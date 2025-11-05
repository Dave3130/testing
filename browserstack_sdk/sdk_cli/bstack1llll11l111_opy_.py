# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1111_opy_,
    bstack1llll111l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll111ll_opy_ import bstack1lllll1111l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1111l1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
class bstack1llllllll1l_opy_(bstack1llll111ll1_opy_):
    bstack1lllllll111_opy_ = bstack11111_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࠨპ")
    bstack1llll1llll1_opy_ = bstack11111_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣჟ")
    bstack1lllll11lll_opy_ = bstack11111_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣრ")
    def __init__(self, bstack1llll11lll1_opy_):
        super().__init__()
        bstack1lllll1111l_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.bstack1llll11llll_opy_, bstack1llllll1111_opy_.PRE), self.bstack1llll1l1l1l_opy_)
        bstack1lllll1111l_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.bstack1lllll1llll_opy_, bstack1llllll1111_opy_.PRE), self.bstack1llllll1ll1_opy_)
        bstack1lllll1111l_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.bstack1lllll1llll_opy_, bstack1llllll1111_opy_.POST), self.bstack1llll11l1l1_opy_)
        bstack1lllll1111l_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.bstack1lllll1llll_opy_, bstack1llllll1111_opy_.POST), self.bstack1lllllllll1_opy_)
        bstack1lllll1111l_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.QUIT, bstack1llllll1111_opy_.POST), self.bstack1lllll1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1l1l1l_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11111_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦს"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11111_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨტ")), str):
                    url = kwargs.get(bstack11111_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢუ"))
                elif hasattr(kwargs.get(bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣფ")), bstack11111_opy_ (u"࠭࡟ࡤ࡮࡬ࡩࡳࡺ࡟ࡤࡱࡱࡪ࡮࡭ࠧქ")):
                    url = kwargs.get(bstack11111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥღ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11111_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦყ"))._url
            except Exception as e:
                url = bstack11111_opy_ (u"ࠩࠪშ")
                self.logger.error(bstack11111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡸࡶࡱࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠾ࠥࢁࡽࠣჩ").format(e))
            self.logger.info(bstack11111_opy_ (u"ࠦࡗ࡫࡭ࡰࡶࡨࠤࡘ࡫ࡲࡷࡧࡵࠤࡆࡪࡤࡳࡧࡶࡷࠥࡨࡥࡪࡰࡪࠤࡵࡧࡳࡴࡧࡧࠤࡦࡹࠠ࠻ࠢࡾࢁࠧც").format(str(url)))
            self.bstack1llll1l11ll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11111_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠳ࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾ࠼ࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥძ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1llllll1ll1_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llllllll1l_opy_.bstack1lllllll111_opy_, False):
            return
        if not f.bstack1llllll1lll_opy_(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_)
        if f.bstack1llllll11ll_opy_(method_name, *args) and len(args) > 1:
            bstack11lll11111_opy_ = datetime.now()
            hub_url = bstack1lllll1111l_opy_.hub_url(driver)
            self.logger.warning(bstack11111_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲ࠽ࠣწ") + str(hub_url) + bstack11111_opy_ (u"ࠢࠣჭ"))
            bstack1lllll1lll1_opy_ = args[1][bstack11111_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢხ")] if isinstance(args[1], dict) and bstack11111_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣჯ") in args[1] else None
            bstack1lllll1l1ll_opy_ = bstack11111_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣჰ")
            if isinstance(bstack1lllll1lll1_opy_, dict):
                bstack11lll11111_opy_ = datetime.now()
                r = self.bstack1lllll1l1l1_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤჱ"), datetime.now() - bstack11lll11111_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11111_opy_ (u"ࠧࡹ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫࠿ࠦࠢჲ") + str(r) + bstack11111_opy_ (u"ࠨࠢჳ"))
                        return
                    if r.hub_url:
                        f.bstack1llll1ll11l_opy_(instance, driver, r.hub_url)
                        f.bstack1lllllll11l_opy_(instance, bstack1llllllll1l_opy_.bstack1lllllll111_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨჴ"), e)
    def bstack1llll11l1l1_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll1111l_opy_.session_id(driver)
            if session_id:
                bstack1lllll11l1l_opy_ = bstack11111_opy_ (u"ࠣࡽࢀ࠾ࡸࡺࡡࡳࡶࠥჵ").format(session_id)
                bstack1llll1ll1l1_opy_.mark(bstack1lllll11l1l_opy_)
    def bstack1lllllllll1_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llllllll1l_opy_.bstack1llll1llll1_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll1111l_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡭ࡻࡢࡠࡷࡵࡰࡂࠨჶ") + str(hub_url) + bstack11111_opy_ (u"ࠥࠦჷ"))
            return
        framework_session_id = bstack1lllll1111l_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢჸ") + str(framework_session_id) + bstack11111_opy_ (u"ࠧࠨჹ"))
            return
        if bstack1lllll1111l_opy_.bstack1llll1ll111_opy_(*args) == bstack1lllll1111l_opy_.bstack1lllll1l111_opy_:
            bstack1llllllll11_opy_ = bstack11111_opy_ (u"ࠨࡻࡾ࠼ࡨࡲࡩࠨჺ").format(framework_session_id)
            bstack1lllll11l1l_opy_ = bstack11111_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤ჻").format(framework_session_id)
            bstack1llll1ll1l1_opy_.end(
                label=bstack11111_opy_ (u"ࠣࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶ࡯ࡴࡶ࠰࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠦჼ"),
                start=bstack1lllll11l1l_opy_,
                end=bstack1llllllll11_opy_,
                status=True,
                failure=None
            )
            bstack11lll11111_opy_ = datetime.now()
            r = self.bstack1llll111lll_opy_(
                ref,
                f.get_state(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣჽ"), datetime.now() - bstack11lll11111_opy_)
            f.bstack1lllllll11l_opy_(instance, bstack1llllllll1l_opy_.bstack1llll1llll1_opy_, r.success)
    def bstack1lllll1ll1l_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llllllll1l_opy_.bstack1lllll11lll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll1111l_opy_.session_id(driver)
        hub_url = bstack1lllll1111l_opy_.hub_url(driver)
        bstack11lll11111_opy_ = datetime.now()
        r = self.bstack1llll1l1lll_opy_(
            ref,
            f.get_state(instance, bstack1lllll1111l_opy_.bstack1lllll1ll11_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1llll1l111_opy_(bstack11111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣჾ"), datetime.now() - bstack11lll11111_opy_)
        f.bstack1lllllll11l_opy_(instance, bstack1llllllll1l_opy_.bstack1lllll11lll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1l1l111l_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1llll1lll1l_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11111_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤჿ") + str(req) + bstack11111_opy_ (u"ࠧࠨᄀ"))
        try:
            r = self.bstack1llll1ll1ll_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤᄁ") + str(r.success) + bstack11111_opy_ (u"ࠢࠣᄂ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᄃ") + str(e) + bstack11111_opy_ (u"ࠤࠥᄄ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll1l11_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1lllll1l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llllll11l1_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11111_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧᄅ") + str(req) + bstack11111_opy_ (u"ࠦࠧᄆ"))
        try:
            r = self.bstack1llll1ll1ll_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣᄇ") + str(r.success) + bstack11111_opy_ (u"ࠨࠢᄈ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᄉ") + str(e) + bstack11111_opy_ (u"ࠣࠤᄊ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1l11l1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1llll111lll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllll11l1_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11111_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶ࠽ࠤࠧᄋ") + str(req) + bstack11111_opy_ (u"ࠥࠦᄌ"))
        try:
            r = self.bstack1llll1ll1ll_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᄍ") + str(r) + bstack11111_opy_ (u"ࠧࠨᄎ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᄏ") + str(e) + bstack11111_opy_ (u"ࠢࠣᄐ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11ll1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1llll1l1lll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllll11l1_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11111_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰ࠻ࠢࠥᄑ") + str(req) + bstack11111_opy_ (u"ࠤࠥᄒ"))
        try:
            r = self.bstack1llll1ll1ll_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᄓ") + str(r) + bstack11111_opy_ (u"ࠦࠧᄔ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᄕ") + str(e) + bstack11111_opy_ (u"ࠨࠢᄖ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11l1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1llll1l11ll_opy_(self, instance: bstack1llll111l1l_opy_, url: str, f: bstack1lllll1111l_opy_, kwargs):
        bstack1llll1l111l_opy_ = version.parse(f.framework_version)
        bstack1llllll111l_opy_ = kwargs.get(bstack11111_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᄗ"))
        bstack1lllll111l1_opy_ = kwargs.get(bstack11111_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄘ"))
        bstack1lllll11111_opy_ = {}
        bstack1llll1l1111_opy_ = {}
        bstack1lllllll1ll_opy_ = None
        bstack1llll1l1ll1_opy_ = {}
        if bstack1lllll111l1_opy_ is not None or bstack1llllll111l_opy_ is not None: # check top level caps
            if bstack1lllll111l1_opy_ is not None:
                bstack1llll1l1ll1_opy_[bstack11111_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᄙ")] = bstack1lllll111l1_opy_
            if bstack1llllll111l_opy_ is not None and callable(getattr(bstack1llllll111l_opy_, bstack11111_opy_ (u"ࠥࡸࡴࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄚ"))):
                bstack1llll1l1ll1_opy_[bstack11111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࡤࡧࡳࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᄛ")] = bstack1llllll111l_opy_.to_capabilities()
        response = self.bstack1llll1lll1l_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1llll1l1ll1_opy_).encode(bstack11111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᄜ")))
        if response is not None and response.capabilities:
            bstack1lllll11111_opy_ = json.loads(response.capabilities.decode(bstack11111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᄝ")))
            if not bstack1lllll11111_opy_: # empty caps bstack1llll11l11l_opy_ bstack1lllll11l11_opy_ bstack1llll1lll11_opy_ bstack1llll11l1ll_opy_ or error in processing
                return
            bstack1lllllll1ll_opy_ = f.bstack1llll1lllll_opy_[bstack11111_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࡠࡨࡵࡳࡲࡥࡣࡢࡲࡶࠦᄞ")](bstack1lllll11111_opy_)
        if bstack1llllll111l_opy_ is not None and bstack1llll1l111l_opy_ >= version.parse(bstack11111_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᄟ")):
            bstack1llll1l1111_opy_ = None
        if (
                not bstack1llllll111l_opy_ and not bstack1lllll111l1_opy_
        ) or (
                bstack1llll1l111l_opy_ < version.parse(bstack11111_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨᄠ"))
        ):
            bstack1llll1l1111_opy_ = {}
            bstack1llll1l1111_opy_.update(bstack1lllll11111_opy_)
        self.logger.info(bstack1111l1lll_opy_)
        if os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨᄡ")).lower().__eq__(bstack11111_opy_ (u"ࠦࡹࡸࡵࡦࠤᄢ")):
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᄣ"): f.bstack1llllll1l1l_opy_,
                }
            )
        if bstack1llll1l111l_opy_ >= version.parse(bstack11111_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ᄤ")):
            if bstack1lllll111l1_opy_ is not None:
                del kwargs[bstack11111_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄥ")]
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᄦ"): bstack1lllllll1ll_opy_,
                    bstack11111_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᄧ"): True,
                    bstack11111_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᄨ"): None,
                }
            )
        elif bstack1llll1l111l_opy_ >= version.parse(bstack11111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪᄩ")):
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄪ"): bstack1llll1l1111_opy_,
                    bstack11111_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᄫ"): bstack1lllllll1ll_opy_,
                    bstack11111_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᄬ"): True,
                    bstack11111_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᄭ"): None,
                }
            )
        elif bstack1llll1l111l_opy_ >= version.parse(bstack11111_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩᄮ")):
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᄯ"): bstack1llll1l1111_opy_,
                    bstack11111_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣᄰ"): True,
                    bstack11111_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᄱ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄲ"): bstack1llll1l1111_opy_,
                    bstack11111_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᄳ"): True,
                    bstack11111_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᄴ"): None,
                }
            )