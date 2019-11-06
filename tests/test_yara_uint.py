test_output="""
{
  "data": "/* trigger = 'deadbeef' */\n(uint32be(0x0) == 0x64656164 and uint32be(0x4) == 0x62656566)",
  "success": true
}
"response=200"
{
  "data": "/* trigger = 'deadbeef' */\n(uint32be(0xa) == 0x64656164 and uint32be(0xe) == 0x62656566)",
  "success": true
}
"response=200"
{
  "data": "/* trigger = 'deadbeef' */\n(uint32be(0xff) == 0x64656164 and uint32be(0x103) == 0x62656566)",
  "success": true
}
"response=200"
{
  "data": "/* trigger = '{deadbeef}' */\n(uint32be(0xff) == 0xdeadbeef)",
  "success": true
}
"""