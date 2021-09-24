/* DEFINE_IME_ENTRY(type, name, params, extended) */
DEFINE_IME_ENTRY(BOOL, ImeInquire, (LPIMEINFO lpIMEInfo, LPVOID lpszWndClass, DWORD dwSystemInfoFlags), FALSE)
DEFINE_IME_ENTRY(DWORD, ImeConversionList, (HIMC hIMC, LPCVOID lpSrc, LPCANDIDATELIST lpDst, DWORD dwBufLen, UINT uFlag), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeRegisterWord, (LPCVOID lpszReading, DWORD dwStyle, LPCVOID lpszString), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeUnregisterWord, (LPCVOID lpszReading, DWORD dwStyle, LPCVOID lpszString), FALSE)
DEFINE_IME_ENTRY(UINT, ImeGetRegisterWordStyle, (UINT nItem, LPVOID lpStyleBuf), FALSE)
DEFINE_IME_ENTRY(UINT, ImeEnumRegisterWord, (LPVOID lpfnEnumProc, LPCVOID lpszReading, DWORD dwStyle, LPCVOID lpszString, LPVOID lpData), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeConfigure, (HKL hKL, HWND hWnd, DWORD dwMode, LPVOID lpData), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeDestroy, (UINT uReserved), FALSE)
DEFINE_IME_ENTRY(LRESULT, ImeEscape, (HIMC hIMC, UINT uEscape, LPVOID lpData), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeProcessKey, (HIMC hIMC, UINT uVirKey, DWORD lParam, CONST LPBYTE lpbKeyState), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeSelect, (HIMC hIMC, BOOL fSelect), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeSetActiveContext, (HIMC hIMC, BOOL fFlag), FALSE)
DEFINE_IME_ENTRY(UINT, ImeToAsciiEx, (UINT uVirKey, UINT uScanCode, CONST LPBYTE lpbKeyState, LPTRANSMSGLIST lpTransMsgList, UINT fuState, HIMC hIMC), FALSE)
DEFINE_IME_ENTRY(BOOL, NotifyIME, (HIMC hIMC, DWORD dwAction, DWORD dwIndex, DWORD dwValue), FALSE)
DEFINE_IME_ENTRY(BOOL, ImeSetCompositionString, (HIMC hIMC, DWORD dwIndex, LPCVOID lpComp, DWORD dwCompLen, LPCVOID lpRead, DWORD dwReadLen), FALSE)
DEFINE_IME_ENTRY(DWORD, ImeGetImeMenuItems, (HIMC hIMC, DWORD dwFlags, DWORD dwType, LPIMEMENUITEMINFOW lpImeParentMenu, LPIMEMENUITEMINFOW lpImeMenu, DWORD dwSize), FALSE)
DEFINE_IME_ENTRY(BOOL, CtfImeInquireExW, (LPIMEINFO lpIMEInfo, LPVOID lpszWndClass, DWORD dwSystemInfoFlags, HKL hKL), TRUE)
DEFINE_IME_ENTRY(BOOL, CtfImeSelectEx, (HIMC hIMC, BOOL fSelect, HKL hKL), TRUE)
DEFINE_IME_ENTRY(LRESULT, CtfImeEscapeEx, (HIMC hIMC, UINT uSubFunc, LPVOID lpData, HKL hKL), TRUE)
DEFINE_IME_ENTRY(DWORD, CtfImeGetGuidAtom, (VOID /* FIXME: unknown */), TRUE)
DEFINE_IME_ENTRY(DWORD, CtfImeIsGuidMapEnable, (VOID /* FIXME: unknown */), TRUE)
