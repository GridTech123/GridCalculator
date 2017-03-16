import cx_Freeze

executables = [cx_Freeze.Executable('Grid_Calculator.py')]

cx_Freeze.setup(name = 'Grid Calculator', version = '1.0.0', options = {'build_exe': {'packages':['spotilib', 'pygame', 'pygame.locals', 'pickle', 'pyError', 'tkFileDialog', 'Grid_Vertex'], 'include_files':['logo.ico',
                                                                                                                                                                                              'logo.png',
                                                                                                                                                                                              'more.png',
                                                                                                                                                                                              'more2.png']}}, executables = executables)
