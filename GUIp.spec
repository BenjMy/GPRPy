# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cli.py'],
             pathex=['E:\\Padova\\Software\\GPRPy'],
             binaries=[],
             datas=[('E:/Padova/Software/GPRPy/gprpy/toolbox/splashdat/A_Square.png', '.'), ('E:/Padova/Software/GPRPy/gprpy/toolbox/splashdat/A_Square_Logo_4c.png', '.'), ('E:/Padova/Software/GPRPy/gprpy/toolbox/splashdat/NSF_4-Color_bitmap_Logo.png', '.'), ('E:/Padova/Software/GPRPy/gprpy/toolbox/splashdat/UA-StackedNameplate.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='GUIp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='GUIp')
