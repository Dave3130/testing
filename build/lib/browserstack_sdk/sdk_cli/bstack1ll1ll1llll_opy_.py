# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll111l1l_opy_ import bstack1llll1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll111l1_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack1lllll11ll1_opy_,
    bstack1llll1ll11l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1llllll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll111ll1l_opy_
from bstack_utils.helper import bstack1lll1lllll1_opy_
import threading
import os
import urllib.parse
class bstack1ll1ll11ll1_opy_(bstack1llll1l1ll1_opy_):
    def __init__(self, bstack1ll1ll11lll_opy_):
        super().__init__()
        bstack1lll1llllll_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_, bstack1lllll11ll1_opy_.PRE), self.bstack1ll1ll1l1ll_opy_)
        bstack1lll1llllll_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_, bstack1lllll11ll1_opy_.PRE), self.bstack1ll1ll111ll_opy_)
        bstack1lll1llllll_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1ll1ll11l1l_opy_, bstack1lllll11ll1_opy_.PRE), self.bstack1ll1ll1l1l1_opy_)
        bstack1lll1llllll_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1llll1l1l1l_opy_, bstack1lllll11ll1_opy_.PRE), self.bstack1ll1ll1l11l_opy_)
        bstack1lll1llllll_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.bstack1llll11ll11_opy_, bstack1lllll11ll1_opy_.PRE), self.bstack1ll1ll1ll1l_opy_)
        bstack1lll1llllll_opy_.bstack1llllll11l1_opy_((bstack1lllllll1ll_opy_.QUIT, bstack1lllll11ll1_opy_.PRE), self.on_close)
        self.bstack1ll1ll11lll_opy_ = bstack1ll1ll11lll_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1ll1l1ll_opy_(
        self,
        f: bstack1lll1llllll_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1111_opy_ (u"ࠤ࡯ࡥࡺࡴࡣࡩࠤᇲ"):
            return
        if not bstack1lll1lllll1_opy_():
            self.logger.debug(bstack11l1111_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢ࡯ࡥࡺࡴࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇳ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, launch, *args, **kwargs):
            response = self.bstack1llll1l1l11_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l1111_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪᇴ"): True}).encode(bstack11l1111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇵ")))
            if response is not None and response.capabilities:
                if not bstack1lll1lllll1_opy_():
                    browser = launch(bstack1ll1ll1lll1_opy_)
                    return browser
                bstack1llll1llll1_opy_ = json.loads(response.capabilities.decode(bstack11l1111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᇶ")))
                if not bstack1llll1llll1_opy_: # empty caps bstack1lllll1l1ll_opy_ bstack1llll1l111l_opy_ bstack1llll1ll1l1_opy_ bstack1llll1l11ll_opy_ or error in processing
                    return
                bstack1ll1ll1l111_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1llll1_opy_))
                f.bstack1llllll1111_opy_(instance, bstack1lll1llllll_opy_.bstack1lll11lll1l_opy_, bstack1ll1ll1l111_opy_)
                f.bstack1llllll1111_opy_(instance, bstack1lll1llllll_opy_.bstack1lll11llll1_opy_, bstack1llll1llll1_opy_)
                browser = bstack1ll1ll1lll1_opy_.connect(bstack1ll1ll1l111_opy_)
                return browser
        return wrapped
    def bstack1ll1ll1l1l1_opy_(
        self,
        f: bstack1lll1llllll_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1111_opy_ (u"ࠢࡥ࡫ࡶࡴࡦࡺࡣࡩࠤᇷ"):
            self.logger.debug(bstack11l1111_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡥ࡫ࡶࡴࡦࡺࡣࡩࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢᇸ"))
            return
        if not bstack1lll1lllll1_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11l1111_opy_ (u"ࠩࡳࡥࡷࡧ࡭ࡴࠩᇹ"), {}).get(bstack11l1111_opy_ (u"ࠪࡦࡸࡖࡡࡳࡣࡰࡷࠬᇺ")):
                    bstack1ll1ll11l11_opy_ = args[0][bstack11l1111_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࡶࠦᇻ")][bstack11l1111_opy_ (u"ࠧࡨࡳࡑࡣࡵࡥࡲࡹࠢᇼ")]
                    session_id = bstack1ll1ll11l11_opy_.get(bstack11l1111_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࡉࡥࠤᇽ"))
                    f.bstack1llllll1111_opy_(instance, bstack1lll1llllll_opy_.bstack1lll1l1l1ll_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11l1111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࠥᇾ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1ll1ll1l_opy_(
        self,
        f: bstack1lll1llllll_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1111_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࠤᇿ"):
            return
        if not bstack1lll1lllll1_opy_():
            self.logger.debug(bstack11l1111_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥࡲࡲࡳ࡫ࡣࡵࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢሀ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, connect, *args, **kwargs):
            response = self.bstack1llll1l1l11_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l1111_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩሁ"): True}).encode(bstack11l1111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥሂ")))
            if response is not None and response.capabilities:
                bstack1llll1llll1_opy_ = json.loads(response.capabilities.decode(bstack11l1111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦሃ")))
                if not bstack1llll1llll1_opy_:
                    return
                bstack1ll1ll1l111_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1llll1_opy_))
                if bstack1llll1llll1_opy_.get(bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬሄ")):
                    browser = bstack1ll1ll1lll1_opy_.connect_over_cdp(bstack1ll1ll1l111_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1ll1l111_opy_
                    return connect(bstack1ll1ll1lll1_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1ll111ll_opy_(
        self,
        f: bstack1lll1llllll_opy_,
        bstack1ll1llll1l1_opy_: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1111_opy_ (u"ࠢ࡯ࡧࡺࡣࡵࡧࡧࡦࠤህ"):
            return
        if not bstack1lll1lllll1_opy_():
            self.logger.debug(bstack11l1111_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡯ࡧࡺࡣࡵࡧࡧࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢሆ"))
            return
        def wrapped(bstack1ll1llll1l1_opy_, bstack1ll1ll1ll11_opy_, *args, **kwargs):
            contexts = bstack1ll1llll1l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack11l1111_opy_ (u"ࠤࡤࡦࡴࡻࡴ࠻ࡤ࡯ࡥࡳࡱࠢሇ") in page.url:
                                    return page
                    else:
                        return bstack1ll1ll1ll11_opy_(bstack1ll1llll1l1_opy_)
        return wrapped
    def bstack1llll1l1l11_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11l1111_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣለ") + str(req) + bstack11l1111_opy_ (u"ࠦࠧሉ"))
        try:
            r = self.bstack1llll1l1lll_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l1111_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣሊ") + str(r.success) + bstack11l1111_opy_ (u"ࠨࠢላ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧሌ") + str(e) + bstack11l1111_opy_ (u"ࠣࠤል"))
            traceback.print_exc()
            raise e
    def bstack1ll1ll1l11l_opy_(
        self,
        f: bstack1lll1llllll_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1111_opy_ (u"ࠤࡢࡷࡪࡴࡤࡠ࡯ࡨࡷࡸࡧࡧࡦࡡࡷࡳࡤࡹࡥࡳࡸࡨࡶࠧሎ"):
            return
        if not bstack1lll1lllll1_opy_():
            return
        def wrapped(Connection, bstack1ll1lll1111_opy_, *args, **kwargs):
            return bstack1ll1lll1111_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1llllll_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1llll1ll11l_opy_, str],
        bstack1llllll1lll_opy_: Tuple[bstack1lllllll1ll_opy_, bstack1lllll11ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1111_opy_ (u"ࠥࡧࡱࡵࡳࡦࠤሏ"):
            return
        if not bstack1lll1lllll1_opy_():
            self.logger.debug(bstack11l1111_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡧࡱࡵࡳࡦࠢࡰࡩࡹ࡮࡯ࡥ࠮ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠢሐ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped