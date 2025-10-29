# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import (
    bstack1lllll1l1ll_opy_,
    bstack1llllll11ll_opy_,
    bstack1llll1llll1_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l1lll1_opy_ import bstack1lll1l111l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l11l11l1l_opy_
from bstack_utils.helper import bstack1lll1l11l11_opy_
import threading
import os
import urllib.parse
class bstack1ll1ll11l11_opy_(bstack1lllll11111_opy_):
    def __init__(self, bstack1ll1ll1lll1_opy_):
        super().__init__()
        bstack1lll1l111l1_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_, bstack1llllll11ll_opy_.PRE), self.bstack1ll1ll1llll_opy_)
        bstack1lll1l111l1_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_, bstack1llllll11ll_opy_.PRE), self.bstack1ll1lll111l_opy_)
        bstack1lll1l111l1_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1ll1ll1l111_opy_, bstack1llllll11ll_opy_.PRE), self.bstack1ll1ll11ll1_opy_)
        bstack1lll1l111l1_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_, bstack1llllll11ll_opy_.PRE), self.bstack1ll1lll1111_opy_)
        bstack1lll1l111l1_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1llllll1lll_opy_, bstack1llllll11ll_opy_.PRE), self.bstack1ll1ll11lll_opy_)
        bstack1lll1l111l1_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.QUIT, bstack1llllll11ll_opy_.PRE), self.on_close)
        self.bstack1ll1ll1lll1_opy_ = bstack1ll1ll1lll1_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1ll1llll_opy_(
        self,
        f: bstack1lll1l111l1_opy_,
        bstack1ll1ll1ll1l_opy_: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11ll_opy_ (u"ࠧࡲࡡࡶࡰࡦ࡬ࠧᇮ"):
            return
        if not bstack1lll1l11l11_opy_():
            self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡲࡡࡶࡰࡦ࡬ࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᇯ"))
            return
        def wrapped(bstack1ll1ll1ll1l_opy_, launch, *args, **kwargs):
            response = self.bstack1lllll11lll_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l11ll_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᇰ"): True}).encode(bstack11l11ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇱ")))
            if response is not None and response.capabilities:
                if not bstack1lll1l11l11_opy_():
                    browser = launch(bstack1ll1ll1ll1l_opy_)
                    return browser
                bstack1llll11l111_opy_ = json.loads(response.capabilities.decode(bstack11l11ll_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇲ")))
                if not bstack1llll11l111_opy_: # empty caps bstack1llll1lll1l_opy_ bstack1llllll1ll1_opy_ bstack1llll11l11l_opy_ bstack1llll11l1ll_opy_ or error in processing
                    return
                bstack1ll1ll1l1l1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll11l111_opy_))
                f.bstack1llll1l1l11_opy_(instance, bstack1lll1l111l1_opy_.bstack1lll1llllll_opy_, bstack1ll1ll1l1l1_opy_)
                f.bstack1llll1l1l11_opy_(instance, bstack1lll1l111l1_opy_.bstack1lll1llll11_opy_, bstack1llll11l111_opy_)
                browser = bstack1ll1ll1ll1l_opy_.connect(bstack1ll1ll1l1l1_opy_)
                return browser
        return wrapped
    def bstack1ll1ll11ll1_opy_(
        self,
        f: bstack1lll1l111l1_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11ll_opy_ (u"ࠥࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠧᇳ"):
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᇴ"))
            return
        if not bstack1lll1l11l11_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11l11ll_opy_ (u"ࠬࡶࡡࡳࡣࡰࡷࠬᇵ"), {}).get(bstack11l11ll_opy_ (u"࠭ࡢࡴࡒࡤࡶࡦࡳࡳࠨᇶ")):
                    bstack1ll1ll1l1ll_opy_ = args[0][bstack11l11ll_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢᇷ")][bstack11l11ll_opy_ (u"ࠣࡤࡶࡔࡦࡸࡡ࡮ࡵࠥᇸ")]
                    session_id = bstack1ll1ll1l1ll_opy_.get(bstack11l11ll_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡌࡨࠧᇹ"))
                    f.bstack1llll1l1l11_opy_(instance, bstack1lll1l111l1_opy_.bstack1lll1l1ll11_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࠨᇺ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1ll11lll_opy_(
        self,
        f: bstack1lll1l111l1_opy_,
        bstack1ll1ll1ll1l_opy_: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11ll_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࠧᇻ"):
            return
        if not bstack1lll1l11l11_opy_():
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡨࡵ࡮࡯ࡧࡦࡸࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥᇼ"))
            return
        def wrapped(bstack1ll1ll1ll1l_opy_, connect, *args, **kwargs):
            response = self.bstack1lllll11lll_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l11ll_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᇽ"): True}).encode(bstack11l11ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᇾ")))
            if response is not None and response.capabilities:
                bstack1llll11l111_opy_ = json.loads(response.capabilities.decode(bstack11l11ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇿ")))
                if not bstack1llll11l111_opy_:
                    return
                bstack1ll1ll1l1l1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll11l111_opy_))
                if bstack1llll11l111_opy_.get(bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨሀ")):
                    browser = bstack1ll1ll1ll1l_opy_.connect_over_cdp(bstack1ll1ll1l1l1_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1ll1l1l1_opy_
                    return connect(bstack1ll1ll1ll1l_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lll111l_opy_(
        self,
        f: bstack1lll1l111l1_opy_,
        bstack1ll1llll11l_opy_: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11ll_opy_ (u"ࠥࡲࡪࡽ࡟ࡱࡣࡪࡩࠧሁ"):
            return
        if not bstack1lll1l11l11_opy_():
            self.logger.debug(bstack11l11ll_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡲࡪࡽ࡟ࡱࡣࡪࡩࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥሂ"))
            return
        def wrapped(bstack1ll1llll11l_opy_, bstack1ll1ll11l1l_opy_, *args, **kwargs):
            contexts = bstack1ll1llll11l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack11l11ll_opy_ (u"ࠧࡧࡢࡰࡷࡷ࠾ࡧࡲࡡ࡯࡭ࠥሃ") in page.url:
                                    return page
                    else:
                        return bstack1ll1ll11l1l_opy_(bstack1ll1llll11l_opy_)
        return wrapped
    def bstack1lllll11lll_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11l11ll_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦሄ") + str(req) + bstack11l11ll_opy_ (u"ࠢࠣህ"))
        try:
            r = self.bstack1llll1l1ll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦሆ") + str(r.success) + bstack11l11ll_opy_ (u"ࠤࠥሇ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣለ") + str(e) + bstack11l11ll_opy_ (u"ࠦࠧሉ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lll1111_opy_(
        self,
        f: bstack1lll1l111l1_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11ll_opy_ (u"ࠧࡥࡳࡦࡰࡧࡣࡲ࡫ࡳࡴࡣࡪࡩࡤࡺ࡯ࡠࡵࡨࡶࡻ࡫ࡲࠣሊ"):
            return
        if not bstack1lll1l11l11_opy_():
            return
        def wrapped(Connection, bstack1ll1ll1ll11_opy_, *args, **kwargs):
            return bstack1ll1ll1ll11_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1l111l1_opy_,
        bstack1ll1ll1ll1l_opy_: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11ll_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࠧላ"):
            return
        if not bstack1lll1l11l11_opy_():
            self.logger.debug(bstack11l11ll_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡣ࡭ࡱࡶࡩࠥࡳࡥࡵࡪࡲࡨ࠱ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠥሌ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped