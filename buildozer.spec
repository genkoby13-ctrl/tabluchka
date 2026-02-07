[app]

# (str) Title of your application
title = Таблиця x÷ Тренажер

# (str) Package name
package.name = tabluchka

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tabluchka

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash background color
android.presplash_color = #F2F2F2

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android build tools version
android.build_tools_version = 33.0.0

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) The archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.native_apis = False

# (str) The format of package name can be either with prefix (default) or without it.
# Android package name must be lowercase. FQDN is required if prefix is used.
# package.domain is enforced in this case.
# N.B.: the prefix is ignored if the first character is a dot.
# android.package_name_format = prefix

# (str) Java source files to include (let empty to not include anything)
#android.add_src =

# (str) AAR libraries to include (currently works only with sdl2_gradle backend)
#android.add_aars =

# (str) Gradle dependencies to add (currently works only with sdl2_gradle backend)
#android.gradle_dependencies =

# (str) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) add Java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
# e.g. android.gradle_repositories =
#     "google()",
#     "jcenter()",
#     "maven { url 'https://kotlin.bintray.com/ktor' }"
android.gradle_repositories =

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
# e.g. android.add_packaging_options =
#     "exclude 'META-INF/common.kotlin_module'",
#     "exclude 'META-INF/*.kotlin_module'"
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, it will not be submitted to the OUYA store.
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs folder. Does not apply to Gradle builds.
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) Android additional libraries to add into the Android project.
#android.add_aars = somepackage.aar

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android project.
#android.add_java_files = org/myorg/mypackage/*.java

# (list) Android additional Java files to add into the Android file.
#android.add_java_files = org/myorg/mypackage/*.java

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display python log
#android.logcat_python_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libs symlink
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
# android.archs = armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aab).
# android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
#p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the result of the p4a build command (set to None to skip the p4a build)
#p4a.binaries_dir =

# (str) The directory in which python-for-android should fill the build
#p4a.build_dir = .p4a/build

# (str) The directory in which python-for-android should fill the dist
#p4a.dist_dir = .p4a/dist

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a kivy-ios checkout:
#ios.kivy_ios_url = https://github.com/kivy/kivy-ios
#ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
#ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
#ios.ios_deploy_branch = 1.7.0

# (bool) Whether or not to sign the code
#ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing the release version
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file
# This option should be defined along with `display-image` and `full-size-image` options.
#ios.manifest.app_url =

# (str) URL pointing to an icon (57x57px)
# This option should be defined along with `app-url` and `full-size-image` options.
#ios.manifest.display_image =

# (str) URL pointing to a large icon (512x512px)
# This option should beply defined along with `app-url` and `display-image` options.
#ios.manifest.full_size_image =

# (str) URL pointing to an icon (57x57px)
# This option should be defined along with `app-url` and `full-size-image` options.
#ios.manifest.display_image =

# (str) URL pointing to a large icon (512x512px)
# This option should beply defined along with `app-url` and `display-image` options.
#ios.manifest.full_size_image =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" sections [list] as:
#
#    [list:key]
#    item1
#    item2
#
#    Or as:
#
#    [list:key]
#    item1,item2
#
#    -----------------------------------------------------------------------------
#
#    You would want to uncomment and edit the following lines to configure
#    your buildozer.ini file to match your requirements.
#
#    [app]
#    title = My Application
#    package.name = myapp
#    package.domain = org.example
#    source.dir = .
#    source.include_exts = py,png,jpg,kv,atlas
#    version = 0.1
#    requirements = python3,kivy
#
#    [android]
#    permissions = INTERNET
#
#    [ios]
#    code_sign.allowed = false
#
#    [buildozer]
#    log_level = 2
#    warn_on_root = 1
#
#    -----------------------------------------------------------------------------

