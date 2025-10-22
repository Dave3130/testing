# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lllll1llll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1lllll11l11_opy_,
    bstack1llll1ll111_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll1ll11ll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll11ll1l1_opy_
from bstack_utils.helper import bstack1lll1ll1lll_opy_
import threading
import os
import urllib.parse
class bstack1ll1ll1l111_opy_(bstack1lllll111l1_opy_):
    def __init__(self, bstack1ll1ll1ll11_opy_):
        super().__init__()
        bstack1lll1ll11ll_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllll11111_opy_, bstack1lllll11l11_opy_.PRE), self.bstack1ll1lll1111_opy_)
        bstack1lll1ll11ll_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllll11111_opy_, bstack1lllll11l11_opy_.PRE), self.bstack1ll1ll11ll1_opy_)
        bstack1lll1ll11ll_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1ll1ll1ll1l_opy_, bstack1lllll11l11_opy_.PRE), self.bstack1ll1ll1llll_opy_)
        bstack1lll1ll11ll_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllllll11l_opy_, bstack1lllll11l11_opy_.PRE), self.bstack1ll1lll11l1_opy_)
        bstack1lll1ll11ll_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.bstack1lllll11111_opy_, bstack1lllll11l11_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1lll1ll11ll_opy_.bstack1lllll1l111_opy_((bstack1llllll1111_opy_.QUIT, bstack1lllll11l11_opy_.PRE), self.on_close)
        self.bstack1ll1ll1ll11_opy_ = bstack1ll1ll1ll11_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll1111_opy_(
        self,
        f: bstack1lll1ll11ll_opy_,
        bstack1ll1ll11lll_opy_: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l111ll_opy_ (u"ࠣ࡮ࡤࡹࡳࡩࡨࠣᇜ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡ࡮ࡤࡹࡳࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇝ"))
            return
        def wrapped(bstack1ll1ll11lll_opy_, launch, *args, **kwargs):
            response = self.bstack1llll11llll_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l111ll_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᇞ"): True}).encode(bstack1l111ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇟ")))
            if response is not None and response.capabilities:
                if not bstack1lll1ll1lll_opy_():
                    browser = launch(bstack1ll1ll11lll_opy_)
                    return browser
                bstack1llll1lllll_opy_ = json.loads(response.capabilities.decode(bstack1l111ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᇠ")))
                if not bstack1llll1lllll_opy_: # empty caps bstack1lllll1l1ll_opy_ bstack1llll1l11ll_opy_ bstack1lllll11ll1_opy_ bstack1llll11l11l_opy_ or error in processing
                    return
                bstack1ll1lll111l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1lllll_opy_))
                f.bstack1lllll1ll1l_opy_(instance, bstack1lll1ll11ll_opy_.bstack1lll1lll1l1_opy_, bstack1ll1lll111l_opy_)
                f.bstack1lllll1ll1l_opy_(instance, bstack1lll1ll11ll_opy_.bstack1lll1lll111_opy_, bstack1llll1lllll_opy_)
                browser = bstack1ll1ll11lll_opy_.connect(bstack1ll1lll111l_opy_)
                return browser
        return wrapped
    def bstack1ll1ll1llll_opy_(
        self,
        f: bstack1lll1ll11ll_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l111ll_opy_ (u"ࠨࡤࡪࡵࡳࡥࡹࡩࡨࠣᇡ"):
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡤࡪࡵࡳࡥࡹࡩࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇢ"))
            return
        if not bstack1lll1ll1lll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1l111ll_opy_ (u"ࠨࡲࡤࡶࡦࡳࡳࠨᇣ"), {}).get(bstack1l111ll_opy_ (u"ࠩࡥࡷࡕࡧࡲࡢ࡯ࡶࠫᇤ")):
                    bstack1ll1ll1lll1_opy_ = args[0][bstack1l111ll_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥᇥ")][bstack1l111ll_opy_ (u"ࠦࡧࡹࡐࡢࡴࡤࡱࡸࠨᇦ")]
                    session_id = bstack1ll1ll1lll1_opy_.get(bstack1l111ll_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡏࡤࠣᇧ"))
                    f.bstack1lllll1ll1l_opy_(instance, bstack1lll1ll11ll_opy_.bstack1llll1111l1_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤᇨ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1lll1ll11ll_opy_,
        bstack1ll1ll11lll_opy_: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l111ll_opy_ (u"ࠢࡤࡱࡱࡲࡪࡩࡴࠣᇩ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1l111ll_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡤࡱࡱࡲࡪࡩࡴࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇪ"))
            return
        def wrapped(bstack1ll1ll11lll_opy_, connect, *args, **kwargs):
            response = self.bstack1llll11llll_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l111ll_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇫ"): True}).encode(bstack1l111ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇬ")))
            if response is not None and response.capabilities:
                bstack1llll1lllll_opy_ = json.loads(response.capabilities.decode(bstack1l111ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇭ")))
                if not bstack1llll1lllll_opy_:
                    return
                bstack1ll1lll111l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1lllll_opy_))
                if bstack1llll1lllll_opy_.get(bstack1l111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫᇮ")):
                    browser = bstack1ll1ll11lll_opy_.connect_over_cdp(bstack1ll1lll111l_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll111l_opy_
                    return connect(bstack1ll1ll11lll_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1ll11ll1_opy_(
        self,
        f: bstack1lll1ll11ll_opy_,
        bstack1ll1llllll1_opy_: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l111ll_opy_ (u"ࠨ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠣᇯ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1l111ll_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦ࡮ࡦࡹࡢࡴࡦ࡭ࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇰ"))
            return
        def wrapped(bstack1ll1llllll1_opy_, bstack1ll1ll1l1l1_opy_, *args, **kwargs):
            contexts = bstack1ll1llllll1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1l111ll_opy_ (u"ࠣࡣࡥࡳࡺࡺ࠺ࡣ࡮ࡤࡲࡰࠨᇱ") in page.url:
                                    return page
                    else:
                        return bstack1ll1ll1l1l1_opy_(bstack1ll1llllll1_opy_)
        return wrapped
    def bstack1llll11llll_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l111ll_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢᇲ") + str(req) + bstack1l111ll_opy_ (u"ࠥࠦᇳ"))
        try:
            r = self.bstack1lllll1lll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢᇴ") + str(r.success) + bstack1l111ll_opy_ (u"ࠧࠨᇵ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᇶ") + str(e) + bstack1l111ll_opy_ (u"ࠢࠣᇷ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lll11l1_opy_(
        self,
        f: bstack1lll1ll11ll_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l111ll_opy_ (u"ࠣࡡࡶࡩࡳࡪ࡟࡮ࡧࡶࡷࡦ࡭ࡥࡠࡶࡲࡣࡸ࡫ࡲࡷࡧࡵࠦᇸ"):
            return
        if not bstack1lll1ll1lll_opy_():
            return
        def wrapped(Connection, bstack1ll1ll1l11l_opy_, *args, **kwargs):
            return bstack1ll1ll1l11l_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1ll11ll_opy_,
        bstack1ll1ll11lll_opy_: object,
        exec: Tuple[bstack1llll1ll111_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1lllll11l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l111ll_opy_ (u"ࠤࡦࡰࡴࡹࡥࠣᇹ"):
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡦࡰࡴࡹࡥࠡ࡯ࡨࡸ࡭ࡵࡤ࠭ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᇺ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped