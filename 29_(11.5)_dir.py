Python 3.8.12 (d00b0afd2a5dd3c13fcda75d738262c864c62fa7, Feb 18 2022, 09:53:04)
[PyPy 7.3.8 with MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys 		# получим список атрибутов модуля 'sys'
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '__warningregistry__', '_base_executable', '_current_frames', '_framework', '_getframe', '_home', '_mercurial', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'pycache_prefix', 'pypy_find_executable', 'pypy_find_stdlib', 'pypy_initfsencoding', 'pypy_objspaceclass', 'pypy_resolvedirof', 'pypy_translation_info', 'pypy_version_info', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> dir() 		# получим список атрибутов текущего модуля
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sys']
>>> a = 5 		# создадим новую переменную 'a'
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'sys']
>>> del a 		# удалим имя 'a'
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'sys']
>>> 