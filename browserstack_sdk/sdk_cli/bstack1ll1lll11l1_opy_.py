# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
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
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lllll111ll_opy_,
    bstack1llllll1l11_opy_,
    bstack1llll11l11l_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1lll1ll_opy_ import bstack1lll1l1l1l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1llll1l1ll_opy_
from bstack_utils.helper import bstack1lll1l11111_opy_
import threading
import os
import urllib.parse
class bstack1ll1ll1l111_opy_(bstack1llllll111l_opy_):
    def __init__(self, bstack1ll1lll11ll_opy_):
        super().__init__()
        bstack1lll1l1l1l1_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llllll1lll_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1ll1ll1llll_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llllll1lll_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1ll1ll1l1ll_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1ll1lll111l_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1ll1ll1ll1l_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1ll1ll1l11l_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llllll1lll_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1ll1ll11lll_opy_)
        bstack1lll1l1l1l1_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.QUIT, bstack1llllll1l11_opy_.PRE), self.on_close)
        self.bstack1ll1lll11ll_opy_ = bstack1ll1lll11ll_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1ll1llll_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1ll1ll11_opy_: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll1_opy_ (u"ࠢ࡭ࡣࡸࡲࡨ࡮ࠢᇛ"):
            return
        if not bstack1lll1l11111_opy_():
            self.logger.debug(bstack11lll1_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡭ࡣࡸࡲࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇜ"))
            return
        def wrapped(bstack1ll1ll1ll11_opy_, launch, *args, **kwargs):
            response = self.bstack1llllll1111_opy_(f.platform_index, instance.ref(), json.dumps({bstack11lll1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇝ"): True}).encode(bstack11lll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇞ")))
            if response is not None and response.capabilities:
                if not bstack1lll1l11111_opy_():
                    browser = launch(bstack1ll1ll1ll11_opy_)
                    return browser
                bstack1llll1l11ll_opy_ = json.loads(response.capabilities.decode(bstack11lll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇟ")))
                if not bstack1llll1l11ll_opy_: # empty caps bstack1lllllll1ll_opy_ bstack1lllll111l1_opy_ bstack11111111l1_opy_ bstack1llll1ll11l_opy_ or error in processing
                    return
                bstack1ll1ll1l1l1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1l11ll_opy_))
                f.bstack1lllll11l11_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1lll1l1l11l_opy_, bstack1ll1ll1l1l1_opy_)
                f.bstack1lllll11l11_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1lll11ll1ll_opy_, bstack1llll1l11ll_opy_)
                browser = bstack1ll1ll1ll11_opy_.connect(bstack1ll1ll1l1l1_opy_)
                return browser
        return wrapped
    def bstack1ll1ll1ll1l_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        Connection: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll1_opy_ (u"ࠧࡪࡩࡴࡲࡤࡸࡨ࡮ࠢᇠ"):
            self.logger.debug(bstack11lll1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇡ"))
            return
        if not bstack1lll1l11111_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11lll1_opy_ (u"ࠧࡱࡣࡵࡥࡲࡹࠧᇢ"), {}).get(bstack11lll1_opy_ (u"ࠨࡤࡶࡔࡦࡸࡡ࡮ࡵࠪᇣ")):
                    bstack1ll1lll1111_opy_ = args[0][bstack11lll1_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᇤ")][bstack11lll1_opy_ (u"ࠥࡦࡸࡖࡡࡳࡣࡰࡷࠧᇥ")]
                    session_id = bstack1ll1lll1111_opy_.get(bstack11lll1_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡎࡪࠢᇦ"))
                    f.bstack1lllll11l11_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1lll1l1l1ll_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11lll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࠣᇧ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1ll11lll_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1ll1ll11_opy_: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll1_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺࠢᇨ"):
            return
        if not bstack1lll1l11111_opy_():
            self.logger.debug(bstack11lll1_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡣࡰࡰࡱࡩࡨࡺࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇩ"))
            return
        def wrapped(bstack1ll1ll1ll11_opy_, connect, *args, **kwargs):
            response = self.bstack1llllll1111_opy_(f.platform_index, instance.ref(), json.dumps({bstack11lll1_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇪ"): True}).encode(bstack11lll1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇫ")))
            if response is not None and response.capabilities:
                bstack1llll1l11ll_opy_ = json.loads(response.capabilities.decode(bstack11lll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇬ")))
                if not bstack1llll1l11ll_opy_:
                    return
                bstack1ll1ll1l1l1_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1llll1l11ll_opy_))
                if bstack1llll1l11ll_opy_.get(bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᇭ")):
                    browser = bstack1ll1ll1ll11_opy_.connect_over_cdp(bstack1ll1ll1l1l1_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1ll1l1l1_opy_
                    return connect(bstack1ll1ll1ll11_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1ll1l1ll_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1lll1ll1_opy_: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll1_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢᇮ"):
            return
        if not bstack1lll1l11111_opy_():
            self.logger.debug(bstack11lll1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡴࡥࡸࡡࡳࡥ࡬࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇯ"))
            return
        def wrapped(bstack1ll1lll1ll1_opy_, bstack1ll1lll1l11_opy_, *args, **kwargs):
            contexts = bstack1ll1lll1ll1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack11lll1_opy_ (u"ࠢࡢࡤࡲࡹࡹࡀࡢ࡭ࡣࡱ࡯ࠧᇰ") in page.url:
                                    return page
                    else:
                        return bstack1ll1lll1l11_opy_(bstack1ll1lll1ll1_opy_)
        return wrapped
    def bstack1llllll1111_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11lll1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨᇱ") + str(req) + bstack11lll1_opy_ (u"ࠤࠥᇲ"))
        try:
            r = self.bstack1llll11lll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11lll1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨᇳ") + str(r.success) + bstack11lll1_opy_ (u"ࠦࠧᇴ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᇵ") + str(e) + bstack11lll1_opy_ (u"ࠨࠢᇶ"))
            traceback.print_exc()
            raise e
    def bstack1ll1ll1l11l_opy_(
        self,
        f: bstack1lll1l1l1l1_opy_,
        Connection: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll1_opy_ (u"ࠢࡠࡵࡨࡲࡩࡥ࡭ࡦࡵࡶࡥ࡬࡫࡟ࡵࡱࡢࡷࡪࡸࡶࡦࡴࠥᇷ"):
            return
        if not bstack1lll1l11111_opy_():
            return
        def wrapped(Connection, bstack1ll1ll1lll1_opy_, *args, **kwargs):
            return bstack1ll1ll1lll1_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll1l1l1l1_opy_,
        bstack1ll1ll1ll11_opy_: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll1_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࠢᇸ"):
            return
        if not bstack1lll1l11111_opy_():
            self.logger.debug(bstack11lll1_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥ࡯ࡳࡸ࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇹ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped