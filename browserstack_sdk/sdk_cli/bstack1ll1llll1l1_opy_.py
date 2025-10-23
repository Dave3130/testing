# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lllll11l1l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l11lll_opy_ import bstack1llll11l1ll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack11l1llll1l_opy_
from bstack_utils.helper import bstack1lll1ll1l1l_opy_
import threading
import os
import urllib.parse
class bstack1ll1lll1ll1_opy_(bstack1llllll111l_opy_):
    def __init__(self, bstack1ll1lllll11_opy_):
        super().__init__()
        bstack1llll11l1ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack111111l111_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1lllllll_opy_)
        bstack1llll11l1ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack111111l111_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1llll11l1ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack1ll1llll11l_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        bstack1llll11l1ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1lll11l1_opy_)
        bstack1llll11l1ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack111111l111_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1ll1llll1ll_opy_)
        bstack1llll11l1ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.QUIT, bstack1llll1ll111_opy_.PRE), self.on_close)
        self.bstack1ll1lllll11_opy_ = bstack1ll1lllll11_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lllllll_opy_(
        self,
        f: bstack1llll11l1ll_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111111l_opy_ (u"ࠥࡰࡦࡻ࡮ࡤࡪࠥᆴ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡰࡦࡻ࡮ࡤࡪࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᆵ"))
            return
        def wrapped(bstack1ll1llll111_opy_, launch, *args, **kwargs):
            response = self.bstack1lllll1lll1_opy_(f.platform_index, instance.ref(), json.dumps({bstack111111l_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᆶ"): True}).encode(bstack111111l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆷ")))
            if response is not None and response.capabilities:
                if not bstack1lll1ll1l1l_opy_():
                    browser = launch(bstack1ll1llll111_opy_)
                    return browser
                bstack1lllll11lll_opy_ = json.loads(response.capabilities.decode(bstack111111l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᆸ")))
                if not bstack1lllll11lll_opy_: # empty caps bstack1llll1llll1_opy_ bstack1lllll11111_opy_ bstack1lllll11l11_opy_ bstack1llll1l1l1l_opy_ or error in processing
                    return
                bstack1ll1lll1l11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllll11lll_opy_))
                f.bstack1llll1lll1l_opy_(instance, bstack1llll11l1ll_opy_.bstack1llll11ll11_opy_, bstack1ll1lll1l11_opy_)
                f.bstack1llll1lll1l_opy_(instance, bstack1llll11l1ll_opy_.bstack1lll1l1ll11_opy_, bstack1lllll11lll_opy_)
                browser = bstack1ll1llll111_opy_.connect(bstack1ll1lll1l11_opy_)
                return browser
        return wrapped
    def bstack1ll1lll1l1l_opy_(
        self,
        f: bstack1llll11l1ll_opy_,
        Connection: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111111l_opy_ (u"ࠣࡦ࡬ࡷࡵࡧࡴࡤࡪࠥᆹ"):
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡦ࡬ࡷࡵࡧࡴࡤࡪࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᆺ"))
            return
        if not bstack1lll1ll1l1l_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack111111l_opy_ (u"ࠪࡴࡦࡸࡡ࡮ࡵࠪᆻ"), {}).get(bstack111111l_opy_ (u"ࠫࡧࡹࡐࡢࡴࡤࡱࡸ࠭ᆼ")):
                    bstack1ll1lll1lll_opy_ = args[0][bstack111111l_opy_ (u"ࠧࡶࡡࡳࡣࡰࡷࠧᆽ")][bstack111111l_opy_ (u"ࠨࡢࡴࡒࡤࡶࡦࡳࡳࠣᆾ")]
                    session_id = bstack1ll1lll1lll_opy_.get(bstack111111l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡊࡦࠥᆿ"))
                    f.bstack1llll1lll1l_opy_(instance, bstack1llll11l1ll_opy_.bstack1lll1lll1ll_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack111111l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡥ࡫ࡶࡴࡦࡺࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࠦᇀ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1llll1ll_opy_(
        self,
        f: bstack1llll11l1ll_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111111l_opy_ (u"ࠤࡦࡳࡳࡴࡥࡤࡶࠥᇁ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡦࡳࡳࡴࡥࡤࡶࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᇂ"))
            return
        def wrapped(bstack1ll1llll111_opy_, connect, *args, **kwargs):
            response = self.bstack1lllll1lll1_opy_(f.platform_index, instance.ref(), json.dumps({bstack111111l_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᇃ"): True}).encode(bstack111111l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇄ")))
            if response is not None and response.capabilities:
                bstack1lllll11lll_opy_ = json.loads(response.capabilities.decode(bstack111111l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᇅ")))
                if not bstack1lllll11lll_opy_:
                    return
                bstack1ll1lll1l11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllll11lll_opy_))
                if bstack1lllll11lll_opy_.get(bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᇆ")):
                    browser = bstack1ll1llll111_opy_.connect_over_cdp(bstack1ll1lll1l11_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll1l11_opy_
                    return connect(bstack1ll1llll111_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1llll11l1ll_opy_,
        bstack1lll11111l1_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111111l_opy_ (u"ࠣࡰࡨࡻࡤࡶࡡࡨࡧࠥᇇ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡰࡨࡻࡤࡶࡡࡨࡧࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᇈ"))
            return
        def wrapped(bstack1lll11111l1_opy_, bstack1ll1llllll1_opy_, *args, **kwargs):
            contexts = bstack1lll11111l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack111111l_opy_ (u"ࠥࡥࡧࡵࡵࡵ࠼ࡥࡰࡦࡴ࡫ࠣᇉ") in page.url:
                                    return page
                    else:
                        return bstack1ll1llllll1_opy_(bstack1lll11111l1_opy_)
        return wrapped
    def bstack1lllll1lll1_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack111111l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤᇊ") + str(req) + bstack111111l_opy_ (u"ࠧࠨᇋ"))
        try:
            r = self.bstack111111111l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack111111l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤᇌ") + str(r.success) + bstack111111l_opy_ (u"ࠢࠣᇍ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᇎ") + str(e) + bstack111111l_opy_ (u"ࠤࠥᇏ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lll11l1_opy_(
        self,
        f: bstack1llll11l1ll_opy_,
        Connection: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111111l_opy_ (u"ࠥࡣࡸ࡫࡮ࡥࡡࡰࡩࡸࡹࡡࡨࡧࡢࡸࡴࡥࡳࡦࡴࡹࡩࡷࠨᇐ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            return
        def wrapped(Connection, bstack1ll1lllll1l_opy_, *args, **kwargs):
            return bstack1ll1lllll1l_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1llll11l1ll_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111111l_opy_ (u"ࠦࡨࡲ࡯ࡴࡧࠥᇑ"):
            return
        if not bstack1lll1ll1l1l_opy_():
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡨࡲ࡯ࡴࡧࠣࡱࡪࡺࡨࡰࡦ࠯ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᇒ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped