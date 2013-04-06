{
  'variables': {
    'homebrew_include%': '<!(brew --prefix)/include',
    'homebrew_lib%': '<!(brew --prefix)/lib'
  },
  'targets': [
    {
      'target_name': 'zmq',
      'sources': [ 'binding.cc' ],
      'conditions': [
        ['OS=="win"', {
          'include_dirs': ['windows/include'],
          'link_settings': {
            'libraries': [
              'Delayimp.lib',
            ],
            'conditions': [
              ['target_arch=="ia32"', {
                'libraries': [
                  '<(PRODUCT_DIR)/../../windows/lib/x86/libzmq-v100-mt-3_2_2.lib',
                ]
              },{
                'libraries': [
                  '<(PRODUCT_DIR)/../../windows/lib/x64/libzmq-v100-mt-3_2_2.lib',
                ]
              }]
            ],
          },
          'msvs_settings': {
            'VCLinkerTool': {
              'DelayLoadDLLs': ['libzmq-v100-mt-3_2_2.dll']
            }
          },
        }, {
          'libraries': ['-lzmq'],
          'cflags!': ['-fno-exceptions'],
          'cflags_cc!': ['-fno-exceptions'],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          },
          'include_dirs': [
            '/opt/local/include',
            '<(homebrew_include)'
          ],
          'libraries': [
            '-L/opt/local/lib',
            '-L<(homebrew_lib)'
          ]
        }],
        ['OS=="linux"', {
          'cflags': [
            '<!(pkg-config libzmq --cflags 2>/dev/null || echo "")',
          ],
          'libraries': [
            '<!(pkg-config libzmq --libs 2>/dev/null || echo "")',
          ],
        }],
      ]
    }
  ]
}
