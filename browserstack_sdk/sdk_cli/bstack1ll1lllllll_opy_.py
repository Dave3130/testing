# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack111111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
    bstack111111lll1_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1l11ll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1111llll1l_opy_
from bstack_utils.helper import bstack1lll1ll1l1l_opy_
import threading
import os
import urllib.parse
class bstack1ll1llll11l_opy_(bstack111111ll11_opy_):
    def __init__(self, bstack1ll1llll111_opy_):
        super().__init__()
        bstack1llll1l11ll_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_, bstack111111111l_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1llll1l11ll_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_, bstack111111111l_opy_.PRE), self.bstack1ll1lllll11_opy_)
        bstack1llll1l11ll_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1ll1lll1ll1_opy_, bstack111111111l_opy_.PRE), self.bstack1ll1llll1ll_opy_)
        bstack1llll1l11ll_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_, bstack111111111l_opy_.PRE), self.bstack1ll1lllll1l_opy_)
        bstack1llll1l11ll_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_, bstack111111111l_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        bstack1llll1l11ll_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.QUIT, bstack111111111l_opy_.PRE), self.on_close)
        self.bstack1ll1llll111_opy_ = bstack1ll1llll111_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1llll1l11ll_opy_,
        bstack1lll1111111_opy_: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll11_opy_ (u"ࠨ࡬ࡢࡷࡱࡧ࡭ࠨᆾ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack1ll11_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦ࡬ࡢࡷࡱࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᆿ"))
            return
        def wrapped(bstack1lll1111111_opy_, launch, *args, **kwargs):
            response = self.bstack1111111111_opy_(f.platform_index, instance.ref(), json.dumps({bstack1ll11_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇀ"): True}).encode(bstack1ll11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇁ")))
            if response is not None and response.capabilities:
                if not bstack1lll1ll1l1l_opy_():
                    browser = launch(bstack1lll1111111_opy_)
                    return browser
                bstack1llllllll1l_opy_ = json.loads(response.capabilities.decode(bstack1ll11_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇂ")))
                if not bstack1llllllll1l_opy_: # empty caps bstack1lllll1l11l_opy_ bstack111111l11l_opy_ bstack1lllll1l111_opy_ bstack1lllll11111_opy_ or error in processing
                    return
                bstack1ll1lll1lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llllllll1l_opy_))
                f.bstack1llll1ll1ll_opy_(instance, bstack1llll1l11ll_opy_.bstack1lll1l1l1ll_opy_, bstack1ll1lll1lll_opy_)
                f.bstack1llll1ll1ll_opy_(instance, bstack1llll1l11ll_opy_.bstack1lll1l1lll1_opy_, bstack1llllllll1l_opy_)
                browser = bstack1lll1111111_opy_.connect(bstack1ll1lll1lll_opy_)
                return browser
        return wrapped
    def bstack1ll1llll1ll_opy_(
        self,
        f: bstack1llll1l11ll_opy_,
        Connection: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll11_opy_ (u"ࠦࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠨᇃ"):
            self.logger.debug(bstack1ll11_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇄ"))
            return
        if not bstack1lll1ll1l1l_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1ll11_opy_ (u"࠭ࡰࡢࡴࡤࡱࡸ࠭ᇅ"), {}).get(bstack1ll11_opy_ (u"ࠧࡣࡵࡓࡥࡷࡧ࡭ࡴࠩᇆ")):
                    bstack1ll1llllll1_opy_ = args[0][bstack1ll11_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᇇ")][bstack1ll11_opy_ (u"ࠤࡥࡷࡕࡧࡲࡢ࡯ࡶࠦᇈ")]
                    session_id = bstack1ll1llllll1_opy_.get(bstack1ll11_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡍࡩࠨᇉ"))
                    f.bstack1llll1ll1ll_opy_(instance, bstack1llll1l11ll_opy_.bstack1lll1ll1l11_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1ll11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠥࡳࡥࡵࡪࡲࡨ࠿ࠦࠢᇊ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll1l1l_opy_(
        self,
        f: bstack1llll1l11ll_opy_,
        bstack1lll1111111_opy_: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll11_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࠨᇋ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack1ll11_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡩ࡯࡯ࡰࡨࡧࡹࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇌ"))
            return
        def wrapped(bstack1lll1111111_opy_, connect, *args, **kwargs):
            response = self.bstack1111111111_opy_(f.platform_index, instance.ref(), json.dumps({bstack1ll11_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᇍ"): True}).encode(bstack1ll11_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇎ")))
            if response is not None and response.capabilities:
                bstack1llllllll1l_opy_ = json.loads(response.capabilities.decode(bstack1ll11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇏ")))
                if not bstack1llllllll1l_opy_:
                    return
                bstack1ll1lll1lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llllllll1l_opy_))
                if bstack1llllllll1l_opy_.get(bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᇐ")):
                    browser = bstack1lll1111111_opy_.connect_over_cdp(bstack1ll1lll1lll_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll1lll_opy_
                    return connect(bstack1lll1111111_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lllll11_opy_(
        self,
        f: bstack1llll1l11ll_opy_,
        bstack1lll11111ll_opy_: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll11_opy_ (u"ࠦࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠨᇑ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack1ll11_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇒ"))
            return
        def wrapped(bstack1lll11111ll_opy_, bstack1ll1llll1l1_opy_, *args, **kwargs):
            contexts = bstack1lll11111ll_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1ll11_opy_ (u"ࠨࡡࡣࡱࡸࡸ࠿ࡨ࡬ࡢࡰ࡮ࠦᇓ") in page.url:
                                    return page
                    else:
                        return bstack1ll1llll1l1_opy_(bstack1lll11111ll_opy_)
        return wrapped
    def bstack1111111111_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1ll11_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡺࡩࡧࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧᇔ") + str(req) + bstack1ll11_opy_ (u"ࠣࠤᇕ"))
        try:
            r = self.bstack1llllll111l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1ll11_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࡷࡺࡩࡣࡦࡵࡶࡁࠧᇖ") + str(r.success) + bstack1ll11_opy_ (u"ࠥࠦᇗ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᇘ") + str(e) + bstack1ll11_opy_ (u"ࠧࠨᇙ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lllll1l_opy_(
        self,
        f: bstack1llll1l11ll_opy_,
        Connection: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll11_opy_ (u"ࠨ࡟ࡴࡧࡱࡨࡤࡳࡥࡴࡵࡤ࡫ࡪࡥࡴࡰࡡࡶࡩࡷࡼࡥࡳࠤᇚ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            return
        def wrapped(Connection, bstack1ll1lll1l11_opy_, *args, **kwargs):
            return bstack1ll1lll1l11_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1llll1l11ll_opy_,
        bstack1lll1111111_opy_: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll11_opy_ (u"ࠢࡤ࡮ࡲࡷࡪࠨᇛ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack1ll11_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡤ࡮ࡲࡷࡪࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇜ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped