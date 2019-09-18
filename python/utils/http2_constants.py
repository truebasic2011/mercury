
HTTP2_MESSAGE_TYPES = {
    0: 'DATA',
    1: 'HEADERS',
    2: 'PRIORITY',
    3: 'RST_STREAM',
    4: 'SETTINGS',
    5: 'PUSH_PROMISE',
    6: 'PING',
    7: 'GOAWAY',
    8: 'WINDOW_UPDATE',
    9: 'CONTINUATION',
}

HTTP2_SETTINGS_TYPES = {
    1: 'HEADER_TABLE_SIZE',
    2: 'ENABLE_PUSH',
    3: 'MAX_CONCURRENT_STREAMS',
    4: 'INITIAL_WINDOW_SIZE',
    5: 'MAX_FRAME_SIZE',
    6: 'MAX_HEADER_LIST_SIZE',
}

HTTP2_ERROR_CODES = {
    0: 'NO_ERROR',
    1: 'PROTOCOL_ERROR',
    2: 'INTERNAL_ERROR',
    3: 'FLOW_CONTROL_ERROR',
    4: 'SETTINGS_TIMEOUT',
    5: 'STREAM_CLOSED',
    6: 'FRAME_SIZE_ERROR',
    7: 'REFUSED_STREAM',
    8: 'CANCEL',
    9: 'COMPRESSION_ERROR',
    10: 'CONNECT_ERROR',
    11: 'ENHANCE_YOUR_CALM',
    12: 'INADEQUATE_SECURITY',
    13: 'HTTP_1_1_REQUIRED',
}
