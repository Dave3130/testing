# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
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
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
    bstack1111111l11_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1l11l1l_opy_ import bstack1lll1l1ll11_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll11l11l_opy_
from bstack_utils.helper import bstack1lll1l1l11l_opy_
import threading
import os
import urllib.parse
class bstack1ll1llll1l1_opy_(bstack1llll1ll11l_opy_):
    def __init__(self, bstack1ll1lll1ll1_opy_):
        super().__init__()
        bstack1lll1l1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1lll1l1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack1ll1lll1lll_opy_)
        bstack1lll1l1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1ll1llll1ll_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack1ll1lllllll_opy_)
        bstack1lll1l1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack1ll1lllll1l_opy_)
        bstack1lll1l1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack1ll1lll1l11_opy_)
        bstack1lll1l1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.QUIT, bstack1lllll1lll1_opy_.PRE), self.on_close)
        self.bstack1ll1lll1ll1_opy_ = bstack1ll1lll1ll1_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1ll1llllll1_opy_: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1_opy_ (u"ࠢ࡭ࡣࡸࡲࡨ࡮ࠢᆿ"):
            return
        if not bstack1lll1l1l11l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡭ࡣࡸࡲࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇀ"))
            return
        def wrapped(bstack1ll1llllll1_opy_, launch, *args, **kwargs):
            response = self.bstack1llllllll1l_opy_(f.platform_index, instance.ref(), json.dumps({bstack1lllll1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇁ"): True}).encode(bstack1lllll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇂ")))
            if response is not None and response.capabilities:
                if not bstack1lll1l1l11l_opy_():
                    browser = launch(bstack1ll1llllll1_opy_)
                    return browser
                bstack111111lll1_opy_ = json.loads(response.capabilities.decode(bstack1lllll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇃ")))
                if not bstack111111lll1_opy_: # empty caps bstack1llllll1111_opy_ bstack1llllll11ll_opy_ bstack1lllll11111_opy_ bstack1lllllll111_opy_ or error in processing
                    return
                bstack1ll1lllll11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack111111lll1_opy_))
                f.bstack1lllll1l11l_opy_(instance, bstack1lll1l1ll11_opy_.bstack1lll1l111l1_opy_, bstack1ll1lllll11_opy_)
                f.bstack1lllll1l11l_opy_(instance, bstack1lll1l1ll11_opy_.bstack1llll11l111_opy_, bstack111111lll1_opy_)
                browser = bstack1ll1llllll1_opy_.connect(bstack1ll1lllll11_opy_)
                return browser
        return wrapped
    def bstack1ll1lllllll_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        Connection: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1_opy_ (u"ࠧࡪࡩࡴࡲࡤࡸࡨ࡮ࠢᇄ"):
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇅ"))
            return
        if not bstack1lll1l1l11l_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1lllll1_opy_ (u"ࠧࡱࡣࡵࡥࡲࡹࠧᇆ"), {}).get(bstack1lllll1_opy_ (u"ࠨࡤࡶࡔࡦࡸࡡ࡮ࡵࠪᇇ")):
                    bstack1ll1llll111_opy_ = args[0][bstack1lllll1_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᇈ")][bstack1lllll1_opy_ (u"ࠥࡦࡸࡖࡡࡳࡣࡰࡷࠧᇉ")]
                    session_id = bstack1ll1llll111_opy_.get(bstack1lllll1_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡎࡪࠢᇊ"))
                    f.bstack1lllll1l11l_opy_(instance, bstack1lll1l1ll11_opy_.bstack1llll1l1l11_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࠣᇋ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll1l11_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1ll1llllll1_opy_: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺࠢᇌ"):
            return
        if not bstack1lll1l1l11l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡣࡰࡰࡱࡩࡨࡺࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇍ"))
            return
        def wrapped(bstack1ll1llllll1_opy_, connect, *args, **kwargs):
            response = self.bstack1llllllll1l_opy_(f.platform_index, instance.ref(), json.dumps({bstack1lllll1_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇎ"): True}).encode(bstack1lllll1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇏ")))
            if response is not None and response.capabilities:
                bstack111111lll1_opy_ = json.loads(response.capabilities.decode(bstack1lllll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇐ")))
                if not bstack111111lll1_opy_:
                    return
                bstack1ll1lllll11_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack111111lll1_opy_))
                if bstack111111lll1_opy_.get(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᇑ")):
                    browser = bstack1ll1llllll1_opy_.connect_over_cdp(bstack1ll1lllll11_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lllll11_opy_
                    return connect(bstack1ll1llllll1_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lll1lll_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1lll111l1l1_opy_: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢᇒ"):
            return
        if not bstack1lll1l1l11l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡴࡥࡸࡡࡳࡥ࡬࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇓ"))
            return
        def wrapped(bstack1lll111l1l1_opy_, bstack1ll1lll1l1l_opy_, *args, **kwargs):
            contexts = bstack1lll111l1l1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1lllll1_opy_ (u"ࠢࡢࡤࡲࡹࡹࡀࡢ࡭ࡣࡱ࡯ࠧᇔ") in page.url:
                                    return page
                    else:
                        return bstack1ll1lll1l1l_opy_(bstack1lll111l1l1_opy_)
        return wrapped
    def bstack1llllllll1l_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨᇕ") + str(req) + bstack1lllll1_opy_ (u"ࠤࠥᇖ"))
        try:
            r = self.bstack1111111l1l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨᇗ") + str(r.success) + bstack1lllll1_opy_ (u"ࠦࠧᇘ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᇙ") + str(e) + bstack1lllll1_opy_ (u"ࠨࠢᇚ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lllll1l_opy_(
        self,
        f: bstack1lll1l1ll11_opy_,
        Connection: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1_opy_ (u"ࠢࡠࡵࡨࡲࡩࡥ࡭ࡦࡵࡶࡥ࡬࡫࡟ࡵࡱࡢࡷࡪࡸࡶࡦࡴࠥᇛ"):
            return
        if not bstack1lll1l1l11l_opy_():
            return
        def wrapped(Connection, bstack1lll1111111_opy_, *args, **kwargs):
            return bstack1lll1111111_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1l1ll11_opy_,
        bstack1ll1llllll1_opy_: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࠢᇜ"):
            return
        if not bstack1lll1l1l11l_opy_():
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥ࡯ࡳࡸ࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇝ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped