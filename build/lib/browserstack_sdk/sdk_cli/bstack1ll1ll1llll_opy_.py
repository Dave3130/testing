# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lllll11l1l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll1l1l1l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll1lll1ll_opy_
from bstack_utils.helper import bstack1lll1l1ll1l_opy_
import threading
import os
import urllib.parse
class bstack1ll1ll1lll1_opy_(bstack1lllllllll1_opy_):
    def __init__(self, bstack1ll1ll1l11l_opy_):
        super().__init__()
        bstack1lll1l1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1llll1_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1ll1lll1111_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1llll1_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1ll1ll1ll11_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1ll1lll111l_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1ll1lll11l1_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1ll1ll1l1ll_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1llll1_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1ll1lll1l11_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.QUIT, bstack1lllll1ll1l_opy_.PRE), self.on_close)
        self.bstack1ll1ll1l11l_opy_ = bstack1ll1ll1l11l_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll1111_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1ll1l111_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll_opy_ (u"ࠣ࡮ࡤࡹࡳࡩࡨࠣᇣ"):
            return
        if not bstack1lll1l1ll1l_opy_():
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡ࡮ࡤࡹࡳࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇤ"))
            return
        def wrapped(bstack1ll1ll1l111_opy_, launch, *args, **kwargs):
            response = self.bstack1llll1lll11_opy_(f.platform_index, instance.ref(), json.dumps({bstack11ll_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᇥ"): True}).encode(bstack11ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇦ")))
            if response is not None and response.capabilities:
                if not bstack1lll1l1ll1l_opy_():
                    browser = launch(bstack1ll1ll1l111_opy_)
                    return browser
                bstack1llllll11l1_opy_ = json.loads(response.capabilities.decode(bstack11ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇧ")))
                if not bstack1llllll11l1_opy_: # empty caps bstack1llllllll11_opy_ bstack1lllll1l111_opy_ bstack1lllll11l11_opy_ bstack1llll11l11l_opy_ or error in processing
                    return
                bstack1ll1ll11lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llllll11l1_opy_))
                f.bstack1llllll1lll_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1lll11lll1l_opy_, bstack1ll1ll11lll_opy_)
                f.bstack1llllll1lll_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1lll1lll1ll_opy_, bstack1llllll11l1_opy_)
                browser = bstack1ll1ll1l111_opy_.connect(bstack1ll1ll11lll_opy_)
                return browser
        return wrapped
    def bstack1ll1lll11l1_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        Connection: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll_opy_ (u"ࠨࡤࡪࡵࡳࡥࡹࡩࡨࠣᇨ"):
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇩ"))
            return
        if not bstack1lll1l1ll1l_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11ll_opy_ (u"ࠨࡲࡤࡶࡦࡳࡳࠨᇪ"), {}).get(bstack11ll_opy_ (u"ࠩࡥࡷࡕࡧࡲࡢ࡯ࡶࠫᇫ")):
                    bstack1ll1lll11ll_opy_ = args[0][bstack11ll_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥᇬ")][bstack11ll_opy_ (u"ࠦࡧࡹࡐࡢࡴࡤࡱࡸࠨᇭ")]
                    session_id = bstack1ll1lll11ll_opy_.get(bstack11ll_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡏࡤࠣᇮ"))
                    f.bstack1llllll1lll_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1lll11llll1_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤᇯ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll1l11_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1ll1l111_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣᇰ"):
            return
        if not bstack1lll1l1ll1l_opy_():
            self.logger.debug(bstack11ll_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡤࡱࡱࡲࡪࡩࡴࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇱ"))
            return
        def wrapped(bstack1ll1ll1l111_opy_, connect, *args, **kwargs):
            response = self.bstack1llll1lll11_opy_(f.platform_index, instance.ref(), json.dumps({bstack11ll_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇲ"): True}).encode(bstack11ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇳ")))
            if response is not None and response.capabilities:
                bstack1llllll11l1_opy_ = json.loads(response.capabilities.decode(bstack11ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇴ")))
                if not bstack1llllll11l1_opy_:
                    return
                bstack1ll1ll11lll_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llllll11l1_opy_))
                if bstack1llllll11l1_opy_.get(bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᇵ")):
                    browser = bstack1ll1ll1l111_opy_.connect_over_cdp(bstack1ll1ll11lll_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1ll11lll_opy_
                    return connect(bstack1ll1ll1l111_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1ll1ll11_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1lll1lll_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll_opy_ (u"ࠨ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠣᇶ"):
            return
        if not bstack1lll1l1ll1l_opy_():
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇷ"))
            return
        def wrapped(bstack1ll1lll1lll_opy_, bstack1ll1ll1ll1l_opy_, *args, **kwargs):
            contexts = bstack1ll1lll1lll_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack11ll_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᇸ") in page.url:
                                    return page
                    else:
                        return bstack1ll1ll1ll1l_opy_(bstack1ll1lll1lll_opy_)
        return wrapped
    def bstack1llll1lll11_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11ll_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢᇹ") + str(req) + bstack11ll_opy_ (u"ࠥࠦᇺ"))
        try:
            r = self.bstack1lllll11111_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11ll_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢᇻ") + str(r.success) + bstack11ll_opy_ (u"ࠧࠨᇼ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᇽ") + str(e) + bstack11ll_opy_ (u"ࠢࠣᇾ"))
            traceback.print_exc()
            raise e
    def bstack1ll1ll1l1ll_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        Connection: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll_opy_ (u"ࠣࡡࡶࡩࡳࡪ࡟࡮ࡧࡶࡷࡦ࡭ࡥࡠࡶࡲࡣࡸ࡫ࡲࡷࡧࡵࠦᇿ"):
            return
        if not bstack1lll1l1ll1l_opy_():
            return
        def wrapped(Connection, bstack1ll1ll1l1l1_opy_, *args, **kwargs):
            return bstack1ll1ll1l1l1_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1ll1l111_opy_: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll_opy_ (u"ࠤࡦࡰࡴࡹࡥࠣሀ"):
            return
        if not bstack1lll1l1ll1l_opy_():
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡦࡰࡴࡹࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨሁ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped