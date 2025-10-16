# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
    bstack1llllll11ll_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1lll1l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1lll1l11ll_opy_
from bstack_utils.helper import bstack1lll1ll1lll_opy_
import threading
import os
import urllib.parse
class bstack1ll1lll1ll1_opy_(bstack1llllllll11_opy_):
    def __init__(self, bstack1ll1lll11ll_opy_):
        super().__init__()
        bstack1lll1lll1l1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1lllll_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1ll1lll1l11_opy_)
        bstack1lll1lll1l1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1lllll_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1ll1lllll11_opy_)
        bstack1lll1lll1l1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1ll1llll1ll_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1ll1lllll1l_opy_)
        bstack1lll1lll1l1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1l1ll1_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1lll1111111_opy_)
        bstack1lll1lll1l1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1lllll_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1ll1lllllll_opy_)
        bstack1lll1lll1l1_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.QUIT, bstack1lllllll1ll_opy_.PRE), self.on_close)
        self.bstack1ll1lll11ll_opy_ = bstack1ll1lll11ll_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll1l11_opy_(
        self,
        f: bstack1lll1lll1l1_opy_,
        bstack1ll1llll1l1_opy_: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1ll1_opy_ (u"ࠣ࡮ࡤࡹࡳࡩࡨࠣᇀ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡ࡮ࡤࡹࡳࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇁ"))
            return
        def wrapped(bstack1ll1llll1l1_opy_, launch, *args, **kwargs):
            response = self.bstack111111l11l_opy_(f.platform_index, instance.ref(), json.dumps({bstack1ll1ll1_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᇂ"): True}).encode(bstack1ll1ll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇃ")))
            if response is not None and response.capabilities:
                if not bstack1lll1ll1lll_opy_():
                    browser = launch(bstack1ll1llll1l1_opy_)
                    return browser
                bstack111111l111_opy_ = json.loads(response.capabilities.decode(bstack1ll1ll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇄ")))
                if not bstack111111l111_opy_: # empty caps bstack1llllll11l1_opy_ bstack111111l1l1_opy_ bstack111111ll1l_opy_ bstack1lllll111l1_opy_ or error in processing
                    return
                bstack1ll1llll111_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack111111l111_opy_))
                f.bstack1lllll1l1ll_opy_(instance, bstack1lll1lll1l1_opy_.bstack1llll11ll1l_opy_, bstack1ll1llll111_opy_)
                f.bstack1lllll1l1ll_opy_(instance, bstack1lll1lll1l1_opy_.bstack1llll111lll_opy_, bstack111111l111_opy_)
                browser = bstack1ll1llll1l1_opy_.connect(bstack1ll1llll111_opy_)
                return browser
        return wrapped
    def bstack1ll1lllll1l_opy_(
        self,
        f: bstack1lll1lll1l1_opy_,
        Connection: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1ll1_opy_ (u"ࠨࡤࡪࡵࡳࡥࡹࡩࡨࠣᇅ"):
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇆ"))
            return
        if not bstack1lll1ll1lll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡶࡦࡳࡳࠨᇇ"), {}).get(bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡕࡧࡲࡢ࡯ࡶࠫᇈ")):
                    bstack1ll1llll11l_opy_ = args[0][bstack1ll1ll1_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥᇉ")][bstack1ll1ll1_opy_ (u"ࠦࡧࡹࡐࡢࡴࡤࡱࡸࠨᇊ")]
                    session_id = bstack1ll1llll11l_opy_.get(bstack1ll1ll1_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡏࡤࠣᇋ"))
                    f.bstack1lllll1l1ll_opy_(instance, bstack1lll1lll1l1_opy_.bstack1lll1l11l1l_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤᇌ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lllllll_opy_(
        self,
        f: bstack1lll1lll1l1_opy_,
        bstack1ll1llll1l1_opy_: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1ll1_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣᇍ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡤࡱࡱࡲࡪࡩࡴࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇎ"))
            return
        def wrapped(bstack1ll1llll1l1_opy_, connect, *args, **kwargs):
            response = self.bstack111111l11l_opy_(f.platform_index, instance.ref(), json.dumps({bstack1ll1ll1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇏ"): True}).encode(bstack1ll1ll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇐ")))
            if response is not None and response.capabilities:
                bstack111111l111_opy_ = json.loads(response.capabilities.decode(bstack1ll1ll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇑ")))
                if not bstack111111l111_opy_:
                    return
                bstack1ll1llll111_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack111111l111_opy_))
                if bstack111111l111_opy_.get(bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᇒ")):
                    browser = bstack1ll1llll1l1_opy_.connect_over_cdp(bstack1ll1llll111_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1llll111_opy_
                    return connect(bstack1ll1llll1l1_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lllll11_opy_(
        self,
        f: bstack1lll1lll1l1_opy_,
        bstack1lll1111l11_opy_: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1ll1_opy_ (u"ࠨ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠣᇓ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇔ"))
            return
        def wrapped(bstack1lll1111l11_opy_, bstack1ll1lll1l1l_opy_, *args, **kwargs):
            contexts = bstack1lll1111l11_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1ll1ll1_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᇕ") in page.url:
                                    return page
                    else:
                        return bstack1ll1lll1l1l_opy_(bstack1lll1111l11_opy_)
        return wrapped
    def bstack111111l11l_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢᇖ") + str(req) + bstack1ll1ll1_opy_ (u"ࠥࠦᇗ"))
        try:
            r = self.bstack1lllll1lll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢᇘ") + str(r.success) + bstack1ll1ll1_opy_ (u"ࠧࠨᇙ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᇚ") + str(e) + bstack1ll1ll1_opy_ (u"ࠢࠣᇛ"))
            traceback.print_exc()
            raise e
    def bstack1lll1111111_opy_(
        self,
        f: bstack1lll1lll1l1_opy_,
        Connection: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1ll1_opy_ (u"ࠣࡡࡶࡩࡳࡪ࡟࡮ࡧࡶࡷࡦ࡭ࡥࡠࡶࡲࡣࡸ࡫ࡲࡷࡧࡵࠦᇜ"):
            return
        if not bstack1lll1ll1lll_opy_():
            return
        def wrapped(Connection, bstack1ll1lll1lll_opy_, *args, **kwargs):
            return bstack1ll1lll1lll_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1lll1l1_opy_,
        bstack1ll1llll1l1_opy_: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1ll1_opy_ (u"ࠤࡦࡰࡴࡹࡥࠣᇝ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡦࡰࡴࡹࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇞ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped