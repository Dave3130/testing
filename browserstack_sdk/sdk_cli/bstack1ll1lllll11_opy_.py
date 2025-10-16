# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack111111l111_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1llll11l1l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1l1ll111_opy_
from bstack_utils.helper import bstack1lll1l1llll_opy_
import threading
import os
import urllib.parse
class bstack1ll1llllll1_opy_(bstack1llll1llll1_opy_):
    def __init__(self, bstack1ll1llll1l1_opy_):
        super().__init__()
        bstack1llll11l1l1_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1llllll1l1l_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1llll11l1l1_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1llllll1l1l_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        bstack1llll11l1l1_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1ll1llll111_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1ll1lll1lll_opy_)
        bstack1llll11l1l1_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1ll1llll1ll_opy_)
        bstack1llll11l1l1_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1llllll1l1l_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1ll1lllll1l_opy_)
        bstack1llll11l1l1_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.QUIT, bstack1llllll1ll1_opy_.PRE), self.on_close)
        self.bstack1ll1llll1l1_opy_ = bstack1ll1llll1l1_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1llll11l1l1_opy_,
        bstack1ll1lllllll_opy_: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l_opy_ (u"ࠤ࡯ࡥࡺࡴࡣࡩࠤᇁ"):
            return
        if not bstack1lll1l1llll_opy_():
            self.logger.debug(bstack1l_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢ࡯ࡥࡺࡴࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇂ"))
            return
        def wrapped(bstack1ll1lllllll_opy_, launch, *args, **kwargs):
            response = self.bstack1lllll111l1_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᇃ"): True}).encode(bstack1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇄ")))
            if response is not None and response.capabilities:
                if not bstack1lll1l1llll_opy_():
                    browser = launch(bstack1ll1lllllll_opy_)
                    return browser
                bstack1llll1ll111_opy_ = json.loads(response.capabilities.decode(bstack1l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᇅ")))
                if not bstack1llll1ll111_opy_: # empty caps bstack1llllllllll_opy_ bstack1lllll111ll_opy_ bstack1lllllllll1_opy_ bstack1llllll1111_opy_ or error in processing
                    return
                bstack1ll1lll1l11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1ll111_opy_))
                f.bstack1lllll11ll1_opy_(instance, bstack1llll11l1l1_opy_.bstack1llll111ll1_opy_, bstack1ll1lll1l11_opy_)
                f.bstack1lllll11ll1_opy_(instance, bstack1llll11l1l1_opy_.bstack1lll1llllll_opy_, bstack1llll1ll111_opy_)
                browser = bstack1ll1lllllll_opy_.connect(bstack1ll1lll1l11_opy_)
                return browser
        return wrapped
    def bstack1ll1lll1lll_opy_(
        self,
        f: bstack1llll11l1l1_opy_,
        Connection: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l_opy_ (u"ࠢࡥ࡫ࡶࡴࡦࡺࡣࡩࠤᇆ"):
            self.logger.debug(bstack1l_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡥ࡫ࡶࡴࡦࡺࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇇ"))
            return
        if not bstack1lll1l1llll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1l_opy_ (u"ࠩࡳࡥࡷࡧ࡭ࡴࠩᇈ"), {}).get(bstack1l_opy_ (u"ࠪࡦࡸࡖࡡࡳࡣࡰࡷࠬᇉ")):
                    bstack1ll1lll1ll1_opy_ = args[0][bstack1l_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᇊ")][bstack1l_opy_ (u"ࠧࡨࡳࡑࡣࡵࡥࡲࡹࠢᇋ")]
                    session_id = bstack1ll1lll1ll1_opy_.get(bstack1l_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࡉࡥࠤᇌ"))
                    f.bstack1lllll11ll1_opy_(instance, bstack1llll11l1l1_opy_.bstack1llll11lll1_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࠥᇍ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lllll1l_opy_(
        self,
        f: bstack1llll11l1l1_opy_,
        bstack1ll1lllllll_opy_: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤᇎ"):
            return
        if not bstack1lll1l1llll_opy_():
            self.logger.debug(bstack1l_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥࡲࡲࡳ࡫ࡣࡵࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇏ"))
            return
        def wrapped(bstack1ll1lllllll_opy_, connect, *args, **kwargs):
            response = self.bstack1lllll111l1_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᇐ"): True}).encode(bstack1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇑ")))
            if response is not None and response.capabilities:
                bstack1llll1ll111_opy_ = json.loads(response.capabilities.decode(bstack1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇒ")))
                if not bstack1llll1ll111_opy_:
                    return
                bstack1ll1lll1l11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1ll111_opy_))
                if bstack1llll1ll111_opy_.get(bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᇓ")):
                    browser = bstack1ll1lllllll_opy_.connect_over_cdp(bstack1ll1lll1l11_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll1l11_opy_
                    return connect(bstack1ll1lllllll_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lll1l1l_opy_(
        self,
        f: bstack1llll11l1l1_opy_,
        bstack1lll111111l_opy_: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤᇔ"):
            return
        if not bstack1lll1l1llll_opy_():
            self.logger.debug(bstack1l_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡯ࡧࡺࡣࡵࡧࡧࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇕ"))
            return
        def wrapped(bstack1lll111111l_opy_, bstack1ll1llll11l_opy_, *args, **kwargs):
            contexts = bstack1lll111111l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1l_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢᇖ") in page.url:
                                    return page
                    else:
                        return bstack1ll1llll11l_opy_(bstack1lll111111l_opy_)
        return wrapped
    def bstack1lllll111l1_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣᇗ") + str(req) + bstack1l_opy_ (u"ࠦࠧᇘ"))
        try:
            r = self.bstack1llll1lll1l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣᇙ") + str(r.success) + bstack1l_opy_ (u"ࠨࠢᇚ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᇛ") + str(e) + bstack1l_opy_ (u"ࠣࠤᇜ"))
            traceback.print_exc()
            raise e
    def bstack1ll1llll1ll_opy_(
        self,
        f: bstack1llll11l1l1_opy_,
        Connection: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l_opy_ (u"ࠤࡢࡷࡪࡴࡤࡠ࡯ࡨࡷࡸࡧࡧࡦࡡࡷࡳࡤࡹࡥࡳࡸࡨࡶࠧᇝ"):
            return
        if not bstack1lll1l1llll_opy_():
            return
        def wrapped(Connection, bstack1lll1111111_opy_, *args, **kwargs):
            return bstack1lll1111111_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1llll11l1l1_opy_,
        bstack1ll1lllllll_opy_: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l_opy_ (u"ࠥࡧࡱࡵࡳࡦࠤᇞ"):
            return
        if not bstack1lll1l1llll_opy_():
            self.logger.debug(bstack1l_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡧࡱࡵࡳࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇟ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped