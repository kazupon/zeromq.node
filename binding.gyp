{
  'variables': {
    'homebrew_include%': '<!(brew --prefix)/include',
    'homebrew_lib%': '<!(brew --prefix)/lib'
  },
  'targets': [
    {
      'target_name': 'binding',
      'sources': [ 'binding.cc' ],
      'libraries': ['-lzmq'],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'conditions': [
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
