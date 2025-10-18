# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
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
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1llll1l1111_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1lll111_opy_ import bstack1lll11ll11l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack111lll1l1_opy_
from bstack_utils.helper import bstack1lll1l11ll1_opy_
import threading
import os
import urllib.parse
class bstack1ll1lll1l11_opy_(bstack1llll1l1l11_opy_):
    def __init__(self, bstack1ll1lll111l_opy_):
        super().__init__()
        bstack1lll11ll11l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llll11llll_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1ll1ll1l111_opy_)
        bstack1lll11ll11l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llll11llll_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1ll1lll11l1_opy_)
        bstack1lll11ll11l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1ll1ll1l11l_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1ll1ll1l1ll_opy_)
        bstack1lll11ll11l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        bstack1lll11ll11l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llll11llll_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1ll1lll1111_opy_)
        bstack1lll11ll11l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.QUIT, bstack1llll1l1lll_opy_.PRE), self.on_close)
        self.bstack1ll1lll111l_opy_ = bstack1ll1lll111l_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1ll1l111_opy_(
        self,
        f: bstack1lll11ll11l_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠨ࡬ࡢࡷࡱࡧ࡭ࠨᇡ"):
            return
        if not bstack1lll1l11ll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦ࡬ࡢࡷࡱࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇢ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, launch, *args, **kwargs):
            response = self.bstack1llll1l111l_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l111_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇣ"): True}).encode(bstack11l111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇤ")))
            if response is not None and response.capabilities:
                if not bstack1lll1l11ll1_opy_():
                    browser = launch(bstack1ll1ll1lll1_opy_)
                    return browser
                bstack1lllll11111_opy_ = json.loads(response.capabilities.decode(bstack11l111_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇥ")))
                if not bstack1lllll11111_opy_: # empty caps bstack1llll1l11ll_opy_ bstack1111111111_opy_ bstack1llllllllll_opy_ bstack1llll11l1l1_opy_ or error in processing
                    return
                bstack1ll1ll1ll1l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllll11111_opy_))
                f.bstack1llllllll1l_opy_(instance, bstack1lll11ll11l_opy_.bstack1llll111ll1_opy_, bstack1ll1ll1ll1l_opy_)
                f.bstack1llllllll1l_opy_(instance, bstack1lll11ll11l_opy_.bstack1lll1ll1111_opy_, bstack1lllll11111_opy_)
                browser = bstack1ll1ll1lll1_opy_.connect(bstack1ll1ll1ll1l_opy_)
                return browser
        return wrapped
    def bstack1ll1ll1l1ll_opy_(
        self,
        f: bstack1lll11ll11l_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠦࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠨᇦ"):
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇧ"))
            return
        if not bstack1lll1l11ll1_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11l111_opy_ (u"࠭ࡰࡢࡴࡤࡱࡸ࠭ᇨ"), {}).get(bstack11l111_opy_ (u"ࠧࡣࡵࡓࡥࡷࡧ࡭ࡴࠩᇩ")):
                    bstack1ll1ll1ll11_opy_ = args[0][bstack11l111_opy_ (u"ࠣࡲࡤࡶࡦࡳࡳࠣᇪ")][bstack11l111_opy_ (u"ࠤࡥࡷࡕࡧࡲࡢ࡯ࡶࠦᇫ")]
                    session_id = bstack1ll1ll1ll11_opy_.get(bstack11l111_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡍࡩࠨᇬ"))
                    f.bstack1llllllll1l_opy_(instance, bstack1lll11ll11l_opy_.bstack1lll1ll1l11_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11l111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡨ࡮ࡹࡰࡢࡶࡦ࡬ࠥࡳࡥࡵࡪࡲࡨ࠿ࠦࠢᇭ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll1111_opy_(
        self,
        f: bstack1lll11ll11l_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠧࡩ࡯࡯ࡰࡨࡧࡹࠨᇮ"):
            return
        if not bstack1lll1l11ll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡩ࡯࡯ࡰࡨࡧࡹࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇯ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, connect, *args, **kwargs):
            response = self.bstack1llll1l111l_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l111_opy_ (u"ࠧࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭ᇰ"): True}).encode(bstack11l111_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇱ")))
            if response is not None and response.capabilities:
                bstack1lllll11111_opy_ = json.loads(response.capabilities.decode(bstack11l111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇲ")))
                if not bstack1lllll11111_opy_:
                    return
                bstack1ll1ll1ll1l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllll11111_opy_))
                if bstack1lllll11111_opy_.get(bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᇳ")):
                    browser = bstack1ll1ll1lll1_opy_.connect_over_cdp(bstack1ll1ll1ll1l_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1ll1ll1l_opy_
                    return connect(bstack1ll1ll1lll1_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lll11l1_opy_(
        self,
        f: bstack1lll11ll11l_opy_,
        bstack1lll1111111_opy_: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠦࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠨᇴ"):
            return
        if not bstack1lll1l11ll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡳ࡫ࡷࡠࡲࡤ࡫ࡪࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇵ"))
            return
        def wrapped(bstack1lll1111111_opy_, bstack1ll1ll1l1l1_opy_, *args, **kwargs):
            contexts = bstack1lll1111111_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack11l111_opy_ (u"ࠨࡡࡣࡱࡸࡸ࠿ࡨ࡬ࡢࡰ࡮ࠦᇶ") in page.url:
                                    return page
                    else:
                        return bstack1ll1ll1l1l1_opy_(bstack1lll1111111_opy_)
        return wrapped
    def bstack1llll1l111l_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11l111_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡺࡩࡧࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧᇷ") + str(req) + bstack11l111_opy_ (u"ࠣࠤᇸ"))
        try:
            r = self.bstack1llllll1l11_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࡷࡺࡩࡣࡦࡵࡶࡁࠧᇹ") + str(r.success) + bstack11l111_opy_ (u"ࠥࠦᇺ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᇻ") + str(e) + bstack11l111_opy_ (u"ࠧࠨᇼ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lll1l1l_opy_(
        self,
        f: bstack1lll11ll11l_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠨ࡟ࡴࡧࡱࡨࡤࡳࡥࡴࡵࡤ࡫ࡪࡥࡴࡰࡡࡶࡩࡷࡼࡥࡳࠤᇽ"):
            return
        if not bstack1lll1l11ll1_opy_():
            return
        def wrapped(Connection, bstack1ll1ll1llll_opy_, *args, **kwargs):
            return bstack1ll1ll1llll_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll11ll11l_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠢࡤ࡮ࡲࡷࡪࠨᇾ"):
            return
        if not bstack1lll1l11ll1_opy_():
            self.logger.debug(bstack11l111_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠࡤ࡮ࡲࡷࡪࠦ࡭ࡦࡶ࡫ࡳࡩ࠲ࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠦᇿ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped