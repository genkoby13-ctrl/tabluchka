from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
import random
import time

# Налаштування кольорів
COLORS = {
    'background': (0.95, 0.95, 0.95, 1),
    'primary': (0.2, 0.6, 0.86, 1),
    'success': (0.3, 0.69, 0.31, 1),
    'danger': (0.96, 0.26, 0.21, 1),
    'warning': (1, 0.76, 0.03, 1),
    'dark': (0.13, 0.13, 0.13, 1),
    'light': (1, 1, 1, 1)
}

class ColoredBoxLayout(BoxLayout):
    """BoxLayout з кольоровим фоном"""
    def __init__(self, color=None, **kwargs):
        super().__init__(**kwargs)
        if color:
            with self.canvas.before:
                Color(*color)
                self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MenuScreen(Screen):
    """Головне меню з налаштуваннями"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = ColoredBoxLayout(orientation='vertical', 
                                      padding=30, 
                                      spacing=20,
                                      color=COLORS['background'])
        
        # Заголовок
        title = Label(text='ТАБЛИЦЯ x÷ ТРЕНАЖЕР', 
                     font_size='32sp',
                     bold=True,
                     color=COLORS['primary'])
        main_layout.add_widget(title)
        
        main_layout.add_widget(Label(text='', size_hint_y=0.1))
        
        # Налаштування діапазону
        range_layout = ColoredBoxLayout(orientation='vertical',
                                       spacing=10,
                                       color=COLORS['light'],
                                       padding=10)
        range_layout.add_widget(Label(text='Діапазон чисел:', 
                                     font_size='20sp',
                                     color=COLORS['dark']))
        
        range_input_layout = BoxLayout(spacing=20)
        range_input_layout.add_widget(Label(text='Від:', size_hint_x=0.2))
        
        self.min_input = TextInput(text='2', 
                                  multiline=False,
                                  input_filter='int',
                                  font_size='24sp',
                                  halign='center',
                                  size_hint_x=0.3)
        range_input_layout.add_widget(self.min_input)
        
        range_input_layout.add_widget(Label(text='До:', size_hint_x=0.2))
        
        self.max_input = TextInput(text='10', 
                                  multiline=False,
                                  input_filter='int',
                                  font_size='24sp',
                                  halign='center',
                                  size_hint_x=0.3)
        range_input_layout.add_widget(self.max_input)
        
        range_layout.add_widget(range_input_layout)
        main_layout.add_widget(range_layout)
        
        # Вибір операцій
        ops_layout = ColoredBoxLayout(orientation='vertical',
                                     spacing=10,
                                     color=COLORS['light'],
                                     padding=10)
        ops_layout.add_widget(Label(text='Оберіть операції:', 
                                   font_size='20sp',
                                   color=COLORS['dark']))
        
        # Множення
        mult_layout = BoxLayout(size_hint_y=0.4)
        self.mult_check = CheckBox(active=True, size_hint_x=0.2)
        mult_layout.add_widget(self.mult_check)
        mult_layout.add_widget(Label(text='Множення (×)', 
                                    font_size='18sp',
                                    color=COLORS['dark']))
        ops_layout.add_widget(mult_layout)
        
        # Ділення
        div_layout = BoxLayout(size_hint_y=0.4)
        self.div_check = CheckBox(active=True, size_hint_x=0.2)
        div_layout.add_widget(self.div_check)
        div_layout.add_widget(Label(text='Ділення (÷)', 
                                   font_size='18sp',
                                   color=COLORS['dark']))
        ops_layout.add_widget(div_layout)
        
        main_layout.add_widget(ops_layout)
        
        main_layout.add_widget(Widget(size_hint_y=0.2))
        
        # Кнопка старту
        start_btn = Button(text='РОЗПОЧАТИ ТРЕНУВАННЯ!',
                          font_size='24sp',
                          bold=True,
                          background_color=COLORS['primary'],
                          size_hint_y=0.15)
        start_btn.bind(on_press=self.start_training)
        main_layout.add_widget(start_btn)
        
        self.add_widget(main_layout)
    
    def start_training(self, instance):
        """Перехід до екрану тренування"""
        try:
            min_num = int(self.min_input.text)
            max_num = int(self.max_input.text)
            
            if min_num < 1 or max_num < min_num:
                raise ValueError("Невірний діапазон")
            
            if not (self.mult_check.active or self.div_check.active):
                raise ValueError("Оберіть хоча б одну операцію")
            
            # Передаємо налаштування
            app = App.get_running_app()
            app.min_number = min_num
            app.max_number = max_num
            app.use_multiplication = self.mult_check.active
            app.use_division = self.div_check.active
            
            # Скидаємо статистику
            app.correct_answers = 0
            app.wrong_answers = 0
            app.start_time = None
            
            # Перехід на екран тренування
            self.manager.current = 'training'
            
        except ValueError as e:
            self.show_error(str(e))
    
    def show_error(self, message):
        """Показати помилку"""
        popup = Popup(title='Помилка',
                     content=Label(text=message),
                     size_hint=(0.8, 0.4))
        popup.open()

class TrainingScreen(Screen):
    """Екран тренування"""
    time_text = StringProperty('00:00')
    stats_text = StringProperty('Правильно: 0 Неправильно: 0')
    question_text = StringProperty('')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_answer = None
        self.timer_event = None
        
        main_layout = ColoredBoxLayout(orientation='vertical',
                                      padding=20,
                                      spacing=15,
                                      color=COLORS['background'])
        
        # Таймер
        self.timer_label = Label(text='00:00',
                                font_size='36sp',
                                bold=True,
                                color=COLORS['primary'])
        main_layout.add_widget(self.timer_label)
        
        # Статистика
        self.stats_label = Label(font_size='22sp',
                                color=COLORS['dark'])
        main_layout.add_widget(self.stats_label)
        
        main_layout.add_widget(Widget(size_hint_y=0.05))
        
        # Область завдання
        task_layout = ColoredBoxLayout(orientation='vertical',
                                      spacing=25,
                                      color=COLORS['light'],
                                      padding=30)
        
        self.question_label = Label(font_size='42sp',
                                   bold=True,
                                   color=COLORS['dark'],
                                   halign='center')
        task_layout.add_widget(self.question_label)
        
        # Поле для відповіді
        self.answer_input = TextInput(multiline=False,
                                     font_size='36sp',
                                     halign='center',
                                     input_filter='int',
                                     size_hint_y=0.4,
                                     hint_text='Введіть відповідь...')
        self.answer_input.bind(on_text_validate=self.check_answer)
        task_layout.add_widget(self.answer_input)
        
        # Кнопка "Наступний"
        next_btn = Button(text='НАСТУПНИЙ',
                         font_size='20sp',
                         background_color=COLORS['primary'],
                         size_hint_y=0.3)
        next_btn.bind(on_press=self.check_answer)
        task_layout.add_widget(next_btn)
        
        main_layout.add_widget(task_layout)
        
        # Кнопка завершення
        finish_btn = Button(text='ЗАВЕРШИТИ',
                           font_size='18sp',
                           background_color=COLORS['danger'],
                           size_hint_y=0.1)
        finish_btn.bind(on_press=self.finish_training)
        main_layout.add_widget(finish_btn)
        
        self.add_widget(main_layout)
    
    def on_enter(self):
        """Коли екран стає активним"""
        # Запуск таймера
        app = App.get_running_app()
        app.start_time = time.time()
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)
        
        # Генерація першого завдання
        self.generate_question()
    
    def on_leave(self):
        """Коли покидаємо екран"""
        if self.timer_event:
            self.timer_event.cancel()
    
    def update_timer(self, dt):
        """Оновлення таймера"""
        app = App.get_running_app()
        if app.start_time:
            elapsed = int(time.time() - app.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.time_text = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.text = self.time_text
    
    def generate_question(self):
        """Генерація нового завдання"""
        app = App.get_running_app()
        min_num = app.min_number
        max_num = app.max_number
        
        # Вибір операції
        operations = []
        if app.use_multiplication:
            operations.append('×')
        if app.use_division:
            operations.append('÷')
        
        operation = random.choice(operations)
        
        if operation == '×':
            # Множення
            a = random.randint(min_num, max_num)
            b = random.randint(min_num, max_num)
            self.question_text = f"{a} × {b} = ?"
            self.current_answer = a * b
        else:
            # Ділення (без остачі)
            a = random.randint(min_num, max_num)
            b = random.randint(min_num, max_num)
            product = a * b
            self.question_text = f"{product} ÷ {a} = ?"
            self.current_answer = b
        
        self.question_label.text = self.question_text
        self.answer_input.text = ''
        self.answer_input.focus = True
    
    def check_answer(self, instance):
        """Перевірка відповіді"""
        user_answer = self.answer_input.text.strip()
        
        if not user_answer:
            return
        
        try:
            user_num = int(user_answer)
            app = App.get_running_app()
            
            if user_num == self.current_answer:
                # Правильна відповідь
                app.correct_answers += 1
                self.answer_input.background_color = COLORS['success'] + (0.3,)
                Clock.schedule_once(lambda dt: setattr(self.answer_input, 'background_color', (1, 1, 1, 1)), 0.5)
            else:
                # Неправильна відповідь
                app.wrong_answers += 1
                self.answer_input.background_color = COLORS['danger'] + (0.3,)
                
                # Показати правильну відповідь
                popup = Popup(title='Правильна відповідь:',
                             content=Label(text=str(self.current_answer),
                                          font_size='24sp'),
                             size_hint=(0.6, 0.3))
                Clock.schedule_once(lambda dt: popup.open(), 0.1)
                Clock.schedule_once(lambda dt: popup.dismiss(), 1.5)
            
            # Оновити статистику
            total = app.correct_answers + app.wrong_answers
            self.stats_text = f"Правильно: {app.correct_answers} Неправильно: {app.wrong_answers}"
            self.stats_label.text = self.stats_text
            
            # Нове завдання
            Clock.schedule_once(lambda dt: self.generate_question(), 0.5)
            
        except ValueError:
            pass
    
    def finish_training(self, instance):
        """Завершити тренування"""
        app = App.get_running_app()
        
        # Зупинити таймер
        if self.timer_event:
            self.timer_event.cancel()
        
        # Розрахувати час
        if app.start_time:
            app.total_time = int(time.time() - app.start_time)
        
        # Перехід до результатів
        self.manager.current = 'results'

class ResultsScreen(Screen):
    """Екран результатів"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = ColoredBoxLayout(orientation='vertical',
                                      padding=30,
                                      spacing=20,
                                      color=COLORS['background'])
        
        # Заголовок
        title = Label(text='РЕЗУЛЬТАТИ',
                     font_size='32sp',
                     bold=True,
                     color=COLORS['primary'])
        main_layout.add_widget(title)
        
        main_layout.add_widget(Widget(size_hint_y=0.1))
        
        # Статистика
        stats_box = ColoredBoxLayout(orientation='vertical',
                                    spacing=15,
                                    color=COLORS['light'],
                                    padding=20)
        
        self.time_label = Label(font_size='24sp', color=COLORS['dark'])
        stats_box.add_widget(self.time_label)
        
        stats_box.add_widget(Widget(size_hint_y=0.1))
        
        self.total_label = Label(font_size='20sp', color=COLORS['dark'])
        stats_box.add_widget(self.total_label)
        
        self.correct_label = Label(font_size='20sp', color=COLORS['success'])
        stats_box.add_widget(self.correct_label)
        
        self.wrong_label = Label(font_size='20sp', color=COLORS['danger'])
        stats_box.add_widget(self.wrong_label)
        
        self.percent_label = Label(font_size='22sp', 
                                  bold=True,
                                  color=COLORS['primary'])
        stats_box.add_widget(self.percent_label)
        
        main_layout.add_widget(stats_box)
        
        main_layout.add_widget(Widget(size_hint_y=0.1))
        
        # Кнопки
        btn_layout = BoxLayout(spacing=20, size_hint_y=0.2)
        
        retry_btn = Button(text='СПРОБУВАТИ ЩЕ',
                          font_size='18sp',
                          background_color=COLORS['warning'])
        retry_btn.bind(on_press=self.retry_training)
        btn_layout.add_widget(retry_btn)
        
        home_btn = Button(text='ГОЛОВНЕ МЕНЮ',
                         font_size='18sp',
                         background_color=COLORS['primary'])
        home_btn.bind(on_press=self.go_home)
        btn_layout.add_widget(home_btn)
        
        main_layout.add_widget(btn_layout)
        
        self.add_widget(main_layout)
    
    def on_enter(self):
        """Коли екран стає активним - показати результати"""
        app = App.get_running_app()
        
        # Час
        minutes = app.total_time // 60
        seconds = app.total_time % 60
        self.time_label.text = f"Час: {minutes:02d}:{seconds:02d}"
        
        # Статистика
        total = app.correct_answers + app.wrong_answers
        self.total_label.text = f"Всього прикладів: {total}"
        self.correct_label.text = f"Правильних: {app.correct_answers}"
        self.wrong_label.text = f"Неправильних: {app.wrong_answers}"
        
        # Відсоток успіху
        if total > 0:
            percent = (app.correct_answers / total) * 100
            self.percent_label.text = f"Успішність: {percent:.1f}%"
        else:
            self.percent_label.text = "Успішність: 0%"
    
    def retry_training(self, instance):
        """Повторити тренування з тими ж налаштуваннями"""
        app = App.get_running_app()
        # Скинути статистику
        app.correct_answers = 0
        app.wrong_answers = 0
        self.manager.current = 'training'
    
    def go_home(self, instance):
        """Повернутися до головного меню"""
        self.manager.current = 'menu'

class MultiplicationTableApp(App):
    """Головний додаток"""
    # Глобальні властивості
    min_number = NumericProperty(2)
    max_number = NumericProperty(10)
    use_multiplication = BooleanProperty(True)
    use_division = BooleanProperty(True)
    correct_answers = NumericProperty(0)
    wrong_answers = NumericProperty(0)
    start_time = None
    total_time = NumericProperty(0)
    
    def build(self):
        self.title = "Таблиця x÷ Тренажер"
        
        # Створення ScreenManager
        sm = ScreenManager()
        
        # Додавання екранів
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(TrainingScreen(name='training'))
        sm.add_widget(ResultsScreen(name='results'))
        
        return sm

if __name__ == '__main__':
    # Налаштування розміру вікна для тестування (тільки для десктопу)
    import platform
    if platform.system() != 'Android':
        Window.size = (400, 700)
    MultiplicationTableApp().run()

