test_output="""{
  "data": [
    {
      "analysis_completed": true,
      "classification": "UNKNOWN",
      "file_type": "XLS",
      "first_seen": "Wed, 16 Oct 2019 16:55:16 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Mon, 28 Oct 2019 06:39:05 GMT",
      "len_code": 8415,
      "len_context": 35268,
      "len_metadata": 11294,
      "len_ocr": 88,
      "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "sha256": "b43e1cef3c40e4629529c0ddcdef3c5be451477afd713abd0b67e1260831ba19",
      "size": 2004642,
      "subcategory": "macro_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule"
    },
    {
      "analysis_completed": true,
      "classification": "UNKNOWN",
      "file_type": "XLS",
      "first_seen": "Wed, 16 Oct 2019 16:55:13 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Sun, 27 Oct 2019 17:28:11 GMT",
      "len_code": 10154,
      "len_context": 20688,
      "len_metadata": 13595,
      "len_ocr": 88,
      "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "sha256": "0d85df8baeedddcf487865eb3bf827399895f1e470675a6542135848514f5003",
      "size": 2044782,
      "subcategory": "macro_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule"
    },
    {
      "analysis_completed": true,
      "classification": "UNKNOWN",
      "file_type": "XLS",
      "first_seen": "Wed, 16 Oct 2019 16:09:02 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Mon, 28 Oct 2019 08:37:09 GMT",
      "len_code": 10508,
      "len_context": 20674,
      "len_metadata": 13595,
      "len_ocr": 88,
      "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "sha256": "cadffb3d09a59d0923ddf57982096383cf44f9016007000a81fa56e875fceaa1",
      "size": 2069673,
      "subcategory": "macro_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/macro_hunter.rule"
    }
  ],
  "success": true
}
"response=200"

"""

"""test dfi_search by md5
{
  "data": [
    {
      "analysis_completed": true,
      "classification": "MALICIOUS",
      "file_type": "OLE",
      "first_seen": "Fri, 08 Jun 2018 22:19:06 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Tue, 22 Oct 2019 21:37:46 GMT",
      "len_code": 0,
      "len_context": 0,
      "len_metadata": 668,
      "len_ocr": 0,
      "mime_type": "application/cdfv2",
      "sha256": "0001104678312b574df5d7fb44da8a2800b48d3442a949ac624064baaa574119",
      "size": 4104,
      "subcategory": "maldoc_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/maldoc_hunter.rule"
    }
  ],
  "success": true
}
"response=200"
"""

"""tes dfi_search by sha1

{
  "data": [
    {
      "analysis_completed": true,
      "classification": "MALICIOUS",
      "file_type": "OLE",
      "first_seen": "Fri, 08 Jun 2018 22:19:06 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Tue, 22 Oct 2019 21:37:46 GMT",
      "len_code": 0,
      "len_context": 0,
      "len_metadata": 668,
      "len_ocr": 0,
      "mime_type": "application/cdfv2",
      "sha256": "0001104678312b574df5d7fb44da8a2800b48d3442a949ac624064baaa574119",
      "size": 4104,
      "subcategory": "maldoc_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/maldoc_hunter.rule"
    }
  ],
  "success": true
}
"""

"""test dfi_search by sha256

{
  "data": [
    {
      "analysis_completed": true,
      "classification": "MALICIOUS",
      "file_type": "OLE",
      "first_seen": "Fri, 08 Jun 2018 22:19:06 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Tue, 22 Oct 2019 21:37:46 GMT",
      "len_code": 0,
      "len_context": 0,
      "len_metadata": 668,
      "len_ocr": 0,
      "mime_type": "application/cdfv2",
      "sha256": "0001104678312b574df5d7fb44da8a2800b48d3442a949ac624064baaa574119",
      "size": 4104,
      "subcategory": "maldoc_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/maldoc_hunter.rule"
    }
  ],
  "success": true
}
"""

""" test dfi_search by sha512

{
  "data": [
    {
      "analysis_completed": true,
      "classification": "MALICIOUS",
      "file_type": "OLE",
      "first_seen": "Fri, 08 Jun 2018 22:19:06 GMT",
      "inquest_alerts": [],
      "last_inquest_featext": "Tue, 22 Oct 2019 21:37:46 GMT",
      "len_code": 0,
      "len_context": 0,
      "len_metadata": 668,
      "len_ocr": 0,
      "mime_type": "application/cdfv2",
      "sha256": "0001104678312b574df5d7fb44da8a2800b48d3442a949ac624064baaa574119",
      "size": 4104,
      "subcategory": "maldoc_hunter",
      "subcategory_url": "https://github.com/InQuest/yara-rules/blob/master/labs.inquest.net/maldoc_hunter.rule"
    }
  ],
  "success": true
}
"response=200"

"""