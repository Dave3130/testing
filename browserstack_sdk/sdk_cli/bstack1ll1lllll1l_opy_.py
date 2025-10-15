# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
    bstack1llllllll1l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l1lll1_opy_ import bstack1lll1l1ll11_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1l111l11_opy_
from bstack_utils.helper import bstack1lll1llll1l_opy_
import threading
import os
import urllib.parse
class bstack1ll1llll11l_opy_(bstack1llll1lll1l_opy_):
    def __init__(self, bstack1ll1lllll11_opy_):
        super().__init__()
        bstack1lll1l1ll11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_, bstack1111111lll_opy_.PRE), self.bstack1ll1lll1lll_opy_)
        bstack1lll1l1ll11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_, bstack1111111lll_opy_.PRE), self.bstack1ll1llll1l1_opy_)
        bstack1lll1l1ll11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1ll1lll1l11_opy_, bstack1111111lll_opy_.PRE), self.bstack1ll1lll11l1_opy_)
        bstack1lll1l1ll11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.PRE), self.bstack1ll1llllll1_opy_)
        bstack1lll1l1ll11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_, bstack1111111lll_opy_.PRE), self.bstack1ll1lll1ll1_opy_)
        bstack1lll1l1ll11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.QUIT, bstack1111111lll_opy_.PRE), self.on_close)
        self.bstack1ll1lllll11_opy_ = bstack1ll1lllll11_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll1lll_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1l_opy_ (u"ࠣ࡮ࡤࡹࡳࡩࡨࠣᆹ"):
            return
        if not bstack1lll1llll1l_opy_():
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡ࡮ࡤࡹࡳࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᆺ"))
            return
        def wrapped(bstack1ll1llll111_opy_, launch, *args, **kwargs):
            response = self.bstack1lllll1l1l1_opy_(f.platform_index, instance.ref(), json.dumps({bstack1ll1l_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᆻ"): True}).encode(bstack1ll1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᆼ")))
            if response is not None and response.capabilities:
                if not bstack1lll1llll1l_opy_():
                    browser = launch(bstack1ll1llll111_opy_)
                    return browser
                bstack11111111l1_opy_ = json.loads(response.capabilities.decode(bstack1ll1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᆽ")))
                if not bstack11111111l1_opy_: # empty caps bstack1llllllllll_opy_ bstack1llll1llll1_opy_ bstack1llll1ll1ll_opy_ bstack11111111ll_opy_ or error in processing
                    return
                bstack1ll1lllllll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack11111111l1_opy_))
                f.bstack1111111ll1_opy_(instance, bstack1lll1l1ll11_opy_.bstack1llll11l11l_opy_, bstack1ll1lllllll_opy_)
                f.bstack1111111ll1_opy_(instance, bstack1lll1l1ll11_opy_.bstack1lll1l1111l_opy_, bstack11111111l1_opy_)
                browser = bstack1ll1llll111_opy_.connect(bstack1ll1lllllll_opy_)
                return browser
        return wrapped
    def bstack1ll1lll11l1_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        Connection: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1l_opy_ (u"ࠨࡤࡪࡵࡳࡥࡹࡩࡨࠣᆾ"):
            self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᆿ"))
            return
        if not bstack1lll1llll1l_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1ll1l_opy_ (u"ࠨࡲࡤࡶࡦࡳࡳࠨᇀ"), {}).get(bstack1ll1l_opy_ (u"ࠩࡥࡷࡕࡧࡲࡢ࡯ࡶࠫᇁ")):
                    bstack1ll1lll1l1l_opy_ = args[0][bstack1ll1l_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥᇂ")][bstack1ll1l_opy_ (u"ࠦࡧࡹࡐࡢࡴࡤࡱࡸࠨᇃ")]
                    session_id = bstack1ll1lll1l1l_opy_.get(bstack1ll1l_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡏࡤࠣᇄ"))
                    f.bstack1111111ll1_opy_(instance, bstack1lll1l1ll11_opy_.bstack1lll1l1llll_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤᇅ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll1ll1_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1l_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣᇆ"):
            return
        if not bstack1lll1llll1l_opy_():
            self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡤࡱࡱࡲࡪࡩࡴࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇇ"))
            return
        def wrapped(bstack1ll1llll111_opy_, connect, *args, **kwargs):
            response = self.bstack1lllll1l1l1_opy_(f.platform_index, instance.ref(), json.dumps({bstack1ll1l_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇈ"): True}).encode(bstack1ll1l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇉ")))
            if response is not None and response.capabilities:
                bstack11111111l1_opy_ = json.loads(response.capabilities.decode(bstack1ll1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇊ")))
                if not bstack11111111l1_opy_:
                    return
                bstack1ll1lllllll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack11111111l1_opy_))
                if bstack11111111l1_opy_.get(bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᇋ")):
                    browser = bstack1ll1llll111_opy_.connect_over_cdp(bstack1ll1lllllll_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lllllll_opy_
                    return connect(bstack1ll1llll111_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1llll1l1_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1lll111l1l1_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1l_opy_ (u"ࠨ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠣᇌ"):
            return
        if not bstack1lll1llll1l_opy_():
            self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇍ"))
            return
        def wrapped(bstack1lll111l1l1_opy_, bstack1ll1lll11ll_opy_, *args, **kwargs):
            contexts = bstack1lll111l1l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1ll1l_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᇎ") in page.url:
                                    return page
                    else:
                        return bstack1ll1lll11ll_opy_(bstack1lll111l1l1_opy_)
        return wrapped
    def bstack1lllll1l1l1_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢᇏ") + str(req) + bstack1ll1l_opy_ (u"ࠥࠦᇐ"))
        try:
            r = self.bstack1llll1l1ll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢᇑ") + str(r.success) + bstack1ll1l_opy_ (u"ࠧࠨᇒ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᇓ") + str(e) + bstack1ll1l_opy_ (u"ࠢࠣᇔ"))
            traceback.print_exc()
            raise e
    def bstack1ll1llllll1_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        Connection: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1l_opy_ (u"ࠣࡡࡶࡩࡳࡪ࡟࡮ࡧࡶࡷࡦ࡭ࡥࡠࡶࡲࡣࡸ࡫ࡲࡷࡧࡵࠦᇕ"):
            return
        if not bstack1lll1llll1l_opy_():
            return
        def wrapped(Connection, bstack1ll1llll1ll_opy_, *args, **kwargs):
            return bstack1ll1llll1ll_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1ll1llll111_opy_: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1l_opy_ (u"ࠤࡦࡰࡴࡹࡥࠣᇖ"):
            return
        if not bstack1lll1llll1l_opy_():
            self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡦࡰࡴࡹࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇗ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped