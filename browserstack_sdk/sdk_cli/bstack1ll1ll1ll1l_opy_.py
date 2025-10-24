# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import json
import os
import grpc
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import bstack1llllll1111_opy_
from browserstack_sdk.sdk_cli.bstack11111111ll_opy_ import (
    bstack1lllllll11l_opy_,
    bstack1llll1l11l1_opy_,
    bstack1lllll111ll_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1lll1lllll1_opy_ import bstack1lll11llll1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1lll1111ll_opy_
from bstack_utils.helper import bstack1lll1l1111l_opy_
import threading
import os
import urllib.parse
class bstack1ll1ll1l1ll_opy_(bstack1llllll1111_opy_):
    def __init__(self, bstack1ll1lll1lll_opy_):
        super().__init__()
        bstack1lll11llll1_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1lllllll111_opy_, bstack1llll1l11l1_opy_.PRE), self.bstack1ll1lll11l1_opy_)
        bstack1lll11llll1_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1lllllll111_opy_, bstack1llll1l11l1_opy_.PRE), self.bstack1ll1lll1l1l_opy_)
        bstack1lll11llll1_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1ll1lll111l_opy_, bstack1llll1l11l1_opy_.PRE), self.bstack1ll1ll1l1l1_opy_)
        bstack1lll11llll1_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1111111l11_opy_, bstack1llll1l11l1_opy_.PRE), self.bstack1ll1lll1l11_opy_)
        bstack1lll11llll1_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1lllllll111_opy_, bstack1llll1l11l1_opy_.PRE), self.bstack1ll1lll11ll_opy_)
        bstack1lll11llll1_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.QUIT, bstack1llll1l11l1_opy_.PRE), self.on_close)
        self.bstack1ll1lll1lll_opy_ = bstack1ll1lll1lll_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1lll11l1_opy_(
        self,
        f: bstack1lll11llll1_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11l1_opy_ (u"ࠢ࡭ࡣࡸࡲࡨ࡮ࠢᇔ"):
            return
        if not bstack1lll1l1111l_opy_():
            self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡔࡨࡸࡺࡸ࡮ࡪࡰࡪࠤ࡮ࡴࠠ࡭ࡣࡸࡲࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇕ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, launch, *args, **kwargs):
            response = self.bstack1llll11lll1_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l11l1_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᇖ"): True}).encode(bstack11l11l1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇗ")))
            if response is not None and response.capabilities:
                if not bstack1lll1l1111l_opy_():
                    browser = launch(bstack1ll1ll1lll1_opy_)
                    return browser
                bstack1lllllllll1_opy_ = json.loads(response.capabilities.decode(bstack11l11l1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᇘ")))
                if not bstack1lllllllll1_opy_: # empty caps bstack1llll1ll1ll_opy_ bstack1llllll1l1l_opy_ bstack1llll1ll111_opy_ bstack1llll1l1111_opy_ or error in processing
                    return
                bstack1ll1lll1111_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllllllll1_opy_))
                f.bstack1llllllllll_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1l1l1l1_opy_, bstack1ll1lll1111_opy_)
                f.bstack1llllllllll_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1lll11l_opy_, bstack1lllllllll1_opy_)
                browser = bstack1ll1ll1lll1_opy_.connect(bstack1ll1lll1111_opy_)
                return browser
        return wrapped
    def bstack1ll1ll1l1l1_opy_(
        self,
        f: bstack1lll11llll1_opy_,
        Connection: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11l1_opy_ (u"ࠧࡪࡩࡴࡲࡤࡸࡨ࡮ࠢᇙ"):
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡪࡩࡴࡲࡤࡸࡨ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇚ"))
            return
        if not bstack1lll1l1111l_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack11l11l1_opy_ (u"ࠧࡱࡣࡵࡥࡲࡹࠧᇛ"), {}).get(bstack11l11l1_opy_ (u"ࠨࡤࡶࡔࡦࡸࡡ࡮ࡵࠪᇜ")):
                    bstack1ll1ll1llll_opy_ = args[0][bstack11l11l1_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᇝ")][bstack11l11l1_opy_ (u"ࠥࡦࡸࡖࡡࡳࡣࡰࡷࠧᇞ")]
                    session_id = bstack1ll1ll1llll_opy_.get(bstack11l11l1_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡎࡪࠢᇟ"))
                    f.bstack1llllllllll_opy_(instance, bstack1lll11llll1_opy_.bstack1lll1l1l11l_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡩ࡯ࡳࡱࡣࡷࡧ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࠣᇠ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1ll1lll11ll_opy_(
        self,
        f: bstack1lll11llll1_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11l1_opy_ (u"ࠨࡣࡰࡰࡱࡩࡨࡺࠢᇡ"):
            return
        if not bstack1lll1l1111l_opy_():
            self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡓࡧࡷࡹࡷࡴࡩ࡯ࡩࠣ࡭ࡳࠦࡣࡰࡰࡱࡩࡨࡺࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇢ"))
            return
        def wrapped(bstack1ll1ll1lll1_opy_, connect, *args, **kwargs):
            response = self.bstack1llll11lll1_opy_(f.platform_index, instance.ref(), json.dumps({bstack11l11l1_opy_ (u"ࠨ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇣ"): True}).encode(bstack11l11l1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᇤ")))
            if response is not None and response.capabilities:
                bstack1lllllllll1_opy_ = json.loads(response.capabilities.decode(bstack11l11l1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᇥ")))
                if not bstack1lllllllll1_opy_:
                    return
                bstack1ll1lll1111_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1lllllllll1_opy_))
                if bstack1lllllllll1_opy_.get(bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᇦ")):
                    browser = bstack1ll1ll1lll1_opy_.connect_over_cdp(bstack1ll1lll1111_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1ll1lll1111_opy_
                    return connect(bstack1ll1ll1lll1_opy_, *args, **kwargs)
        return wrapped
    def bstack1ll1lll1l1l_opy_(
        self,
        f: bstack1lll11llll1_opy_,
        bstack1ll1lllll1l_opy_: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11l1_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢᇧ"):
            return
        if not bstack1lll1l1111l_opy_():
            self.logger.debug(bstack11l11l1_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡴࡥࡸࡡࡳࡥ࡬࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇨ"))
            return
        def wrapped(bstack1ll1lllll1l_opy_, bstack1ll1ll1ll11_opy_, *args, **kwargs):
            contexts = bstack1ll1lllll1l_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack11l11l1_opy_ (u"ࠢࡢࡤࡲࡹࡹࡀࡢ࡭ࡣࡱ࡯ࠧᇩ") in page.url:
                                    return page
                    else:
                        return bstack1ll1ll1ll11_opy_(bstack1ll1lllll1l_opy_)
        return wrapped
    def bstack1llll11lll1_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨᇪ") + str(req) + bstack11l11l1_opy_ (u"ࠤࠥᇫ"))
        try:
            r = self.bstack1lllllll1ll_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨᇬ") + str(r.success) + bstack11l11l1_opy_ (u"ࠦࠧᇭ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᇮ") + str(e) + bstack11l11l1_opy_ (u"ࠨࠢᇯ"))
            traceback.print_exc()
            raise e
    def bstack1ll1lll1l11_opy_(
        self,
        f: bstack1lll11llll1_opy_,
        Connection: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11l1_opy_ (u"ࠢࡠࡵࡨࡲࡩࡥ࡭ࡦࡵࡶࡥ࡬࡫࡟ࡵࡱࡢࡷࡪࡸࡶࡦࡴࠥᇰ"):
            return
        if not bstack1lll1l1111l_opy_():
            return
        def wrapped(Connection, bstack1ll1lll1ll1_opy_, *args, **kwargs):
            return bstack1ll1lll1ll1_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1lll11llll1_opy_,
        bstack1ll1ll1lll1_opy_: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l11l1_opy_ (u"ࠣࡥ࡯ࡳࡸ࡫ࠢᇱ"):
            return
        if not bstack1lll1l1111l_opy_():
            self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡕࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥ࡯࡮ࠡࡥ࡯ࡳࡸ࡫ࠠ࡮ࡧࡷ࡬ࡴࡪࠬࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᇲ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped