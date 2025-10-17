# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import bstack1llll1l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import (
    bstack1lllll11111_opy_,
    bstack1llllllll1l_opy_,
    bstack1llllll1lll_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l111ll_opy_ import bstack1lll1ll1ll1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack11l1l111ll_opy_
from bstack_utils.helper import bstack1lll11llll1_opy_
import threading
import os
import urllib.parse
class bstack1ll1llll111_opy_(bstack1llll1l1l1l_opy_):
    def __init__(self, bstack1ll1lll11l1_opy_):
        super().__init__()
        bstack1lll1ll1ll1_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.bstack1lllll11lll_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1ll1llll11l_opy_)
        bstack1lll1ll1ll1_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.bstack1lllll11lll_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1ll1lll1ll1_opy_)
        bstack1lll1ll1ll1_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.bstack1ll1ll1llll_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1ll1lll1l11_opy_)
        bstack1lll1ll1ll1_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.bstack1llll1lllll_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1ll1llll1ll_opy_)
        bstack1lll1ll1ll1_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.bstack1lllll11lll_opy_, bstack1llllllll1l_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1lll1ll1ll1_opy_.bstack1llll1llll1_opy_((bstack1lllll11111_opy_.QUIT, bstack1llllllll1l_opy_.PRE), self.on_close)
        self.bstack1ll1lll11l1_opy_ = bstack1ll1lll11l1_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1llll11l_opy_(
        self,
        f: bstack1lll1ll1ll1_opy_,
        bstack1ll1lll1l1l_opy_: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠦࡱࡧࡵ࡯ࡥ࡫ࠦᆮ"):
            return
        if not bstack1lll11llll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡱࡧࡵ࡯ࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᆯ"))
            return
        def wrapped(bstack1ll1lll1l1l_opy_, launch, *args, **kwargs):
            response = self.bstack1llllllll11_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l111_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬᆰ"): True}).encode(bstack11l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᆱ")))
            if response is not None and response.capabilities:
                if not bstack1lll11llll1_opy_():
                    browser = launch(bstack1ll1lll1l1l_opy_)
                    return browser
                bstack1llll1lll1l_opy_ = json.loads(response.capabilities.decode(bstack11l111_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᆲ")))
                if not bstack1llll1lll1l_opy_: # empty caps bstack111111l1l1_opy_ bstack1lllllll1l1_opy_ bstack1llll1l1ll1_opy_ bstack111111l111_opy_ or error in processing
                    return
                bstack1ll1lll111l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1lll1l_opy_))
                f.bstack1lllll111ll_opy_(instance, bstack1lll1ll1ll1_opy_.bstack1lll1l1l11l_opy_, bstack1ll1lll111l_opy_)
                f.bstack1lllll111ll_opy_(instance, bstack1lll1ll1ll1_opy_.bstack1lll1l1llll_opy_, bstack1llll1lll1l_opy_)
                browser = bstack1ll1lll1l1l_opy_.connect(bstack1ll1lll111l_opy_)
                return browser
        return wrapped
    def bstack1ll1lll1l11_opy_(
        self,
        f: bstack1lll1ll1ll1_opy_,
        Connection: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠤࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠦᆳ"):
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᆴ"))
            return
        if not bstack1lll11llll1_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11l111_opy_ (u"ࠫࡵࡧࡲࡢ࡯ࡶࠫᆵ"), {}).get(bstack11l111_opy_ (u"ࠬࡨࡳࡑࡣࡵࡥࡲࡹࠧᆶ")):
                    bstack1ll1lll1111_opy_ = args[0][bstack11l111_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᆷ")][bstack11l111_opy_ (u"ࠢࡣࡵࡓࡥࡷࡧ࡭ࡴࠤᆸ")]
                    session_id = bstack1ll1lll1111_opy_.get(bstack11l111_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡋࡧࠦᆹ"))
                    f.bstack1lllll111ll_opy_(instance, bstack1lll1ll1ll1_opy_.bstack1llll111l11_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11l111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡦ࡬ࡷࡵࡧࡴࡤࡪࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࠧᆺ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1lll1ll1ll1_opy_,
        bstack1ll1lll1l1l_opy_: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࠦᆻ"):
            return
        if not bstack1lll11llll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡧࡴࡴ࡮ࡦࡥࡷࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᆼ"))
            return
        def wrapped(bstack1ll1lll1l1l_opy_, connect, *args, **kwargs):
            response = self.bstack1llllllll11_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l111_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫᆽ"): True}).encode(bstack11l111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᆾ")))
            if response is not None and response.capabilities:
                bstack1llll1lll1l_opy_ = json.loads(response.capabilities.decode(bstack11l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᆿ")))
                if not bstack1llll1lll1l_opy_:
                    return
                bstack1ll1lll111l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1lll1l_opy_))
                if bstack1llll1lll1l_opy_.get(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᇀ")):
                    browser = bstack1ll1lll1l1l_opy_.connect_over_cdp(bstack1ll1lll111l_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll111l_opy_
                    return connect(bstack1ll1lll1l1l_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lll1ll1_opy_(
        self,
        f: bstack1lll1ll1ll1_opy_,
        bstack1lll1111l1l_opy_: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦᇁ"):
            return
        if not bstack1lll11llll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡱࡩࡼࡥࡰࡢࡩࡨࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᇂ"))
            return
        def wrapped(bstack1lll1111l1l_opy_, bstack1ll1llll1l1_opy_, *args, **kwargs):
            contexts = bstack1lll1111l1l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack11l111_opy_ (u"ࠦࡦࡨ࡯ࡶࡶ࠽ࡦࡱࡧ࡮࡬ࠤᇃ") in page.url:
                                    return page
                    else:
                        return bstack1ll1llll1l1_opy_(bstack1lll1111l1l_opy_)
        return wrapped
    def bstack1llllllll11_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11l111_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥᇄ") + str(req) + bstack11l111_opy_ (u"ࠨࠢᇅ"))
        try:
            r = self.bstack1lllllllll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥᇆ") + str(r.success) + bstack11l111_opy_ (u"ࠣࠤᇇ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᇈ") + str(e) + bstack11l111_opy_ (u"ࠥࠦᇉ"))
            traceback.print_exc()
            raise e
    def bstack1ll1llll1ll_opy_(
        self,
        f: bstack1lll1ll1ll1_opy_,
        Connection: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠦࡤࡹࡥ࡯ࡦࡢࡱࡪࡹࡳࡢࡩࡨࡣࡹࡵ࡟ࡴࡧࡵࡺࡪࡸࠢᇊ"):
            return
        if not bstack1lll11llll1_opy_():
            return
        def wrapped(Connection, bstack1ll1lllll11_opy_, *args, **kwargs):
            return bstack1ll1lllll11_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1ll1ll1_opy_,
        bstack1ll1lll1l1l_opy_: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦᇋ"):
            return
        if not bstack1lll11llll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡩ࡬ࡰࡵࡨࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤᇌ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped