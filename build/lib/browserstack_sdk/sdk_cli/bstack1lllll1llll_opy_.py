# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1111111lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1llll1l11ll_opy_,
    bstack1llll1l1l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1l11_opy_ import bstack1llll1l11l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll1lllll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11l1ll11l_opy_ import bstack111111l11l_opy_
class bstack1lllllll1l1_opy_(bstack1lllll1l1l1_opy_):
    bstack1lllll111l1_opy_ = bstack11111_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴࠣႚ")
    bstack111111l1ll_opy_ = bstack11111_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥႛ")
    bstack1111111111_opy_ = bstack11111_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥႜ")
    def __init__(self, bstack111111l1l1_opy_):
        super().__init__()
        bstack1llll1l11l1_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll11l1_opy_, bstack1llll1l11ll_opy_.PRE), self.bstack1111111ll1_opy_)
        bstack1llll1l11l1_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll1lll_opy_, bstack1llll1l11ll_opy_.PRE), self.bstack1llll1ll11l_opy_)
        bstack1llll1l11l1_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll1lll_opy_, bstack1llll1l11ll_opy_.POST), self.bstack1lllllll11l_opy_)
        bstack1llll1l11l1_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll1lll_opy_, bstack1llll1l11ll_opy_.POST), self.bstack11111111l1_opy_)
        bstack1llll1l11l1_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.QUIT, bstack1llll1l11ll_opy_.POST), self.bstack111111111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1111111ll1_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11111_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨႝ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣ႞")), str):
                    url = kwargs.get(bstack11111_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤ႟"))
                elif hasattr(kwargs.get(bstack11111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥႠ")), bstack11111_opy_ (u"ࠨࡡࡦࡰ࡮࡫࡮ࡵࡡࡦࡳࡳ࡬ࡩࡨࠩႡ")):
                    url = kwargs.get(bstack11111_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧႢ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11111_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨႣ"))._url
            except Exception as e:
                url = bstack11111_opy_ (u"ࠫࠬႤ")
                self.logger.error(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡺࡸ࡬ࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷࡀࠠࡼࡿࠥႥ").format(e))
            self.logger.info(bstack11111_opy_ (u"ࠨࡒࡦ࡯ࡲࡸࡪࠦࡓࡦࡴࡹࡩࡷࠦࡁࡥࡦࡵࡩࡸࡹࠠࡣࡧ࡬ࡲ࡬ࠦࡰࡢࡵࡶࡩࡩࠦࡡࡴࠢ࠽ࠤࢀࢃࠢႦ").format(str(url)))
            self.bstack1llllllllll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11111_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠮ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀ࠾ࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧႧ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1llll1ll11l_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1lllllll1l1_opy_.bstack1lllll111l1_opy_, False):
            return
        if not f.bstack1llllllll1l_opy_(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_):
            return
        platform_index = f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_)
        if f.bstack1lllll1l11l_opy_(method_name, *args) and len(args) > 1:
            bstack1lll11l111_opy_ = datetime.now()
            hub_url = bstack1llll1l11l1_opy_.hub_url(driver)
            self.logger.warning(bstack11111_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭࠿ࠥႨ") + str(hub_url) + bstack11111_opy_ (u"ࠤࠥႩ"))
            bstack1llll1ll111_opy_ = args[1][bstack11111_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤႪ")] if isinstance(args[1], dict) and bstack11111_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥႫ") in args[1] else None
            bstack1llll1l1lll_opy_ = bstack11111_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥႬ")
            if isinstance(bstack1llll1ll111_opy_, dict):
                bstack1lll11l111_opy_ = datetime.now()
                r = self.bstack1lllll1l1ll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦႭ"), datetime.now() - bstack1lll11l111_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11111_opy_ (u"ࠢࡴࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭࠺ࠡࠤႮ") + str(r) + bstack11111_opy_ (u"ࠣࠤႯ"))
                        return
                    if r.hub_url:
                        f.bstack1llllll1l1l_opy_(instance, driver, r.hub_url)
                        f.bstack11111111ll_opy_(instance, bstack1lllllll1l1_opy_.bstack1lllll111l1_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11111_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣႰ"), e)
    def bstack1lllllll11l_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llll1l11l1_opy_.session_id(driver)
            if session_id:
                bstack1lllll111ll_opy_ = bstack11111_opy_ (u"ࠥࡿࢂࡀࡳࡵࡣࡵࡸࠧႱ").format(session_id)
                bstack111111l11l_opy_.mark(bstack1lllll111ll_opy_)
    def bstack11111111l1_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllllll1l1_opy_.bstack111111l1ll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llll1l11l1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣႲ") + str(hub_url) + bstack11111_opy_ (u"ࠧࠨႳ"))
            return
        framework_session_id = bstack1llll1l11l1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤႴ") + str(framework_session_id) + bstack11111_opy_ (u"ࠢࠣႵ"))
            return
        if bstack1llll1l11l1_opy_.bstack1lllllllll1_opy_(*args) == bstack1llll1l11l1_opy_.bstack1llllll1ll1_opy_:
            bstack1111111l11_opy_ = bstack11111_opy_ (u"ࠣࡽࢀ࠾ࡪࡴࡤࠣႶ").format(framework_session_id)
            bstack1lllll111ll_opy_ = bstack11111_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦႷ").format(framework_session_id)
            bstack111111l11l_opy_.end(
                label=bstack11111_opy_ (u"ࠥࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡱࡶࡸ࠲࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳࠨႸ"),
                start=bstack1lllll111ll_opy_,
                end=bstack1111111l11_opy_,
                status=True,
                failure=None
            )
            bstack1lll11l111_opy_ = datetime.now()
            r = self.bstack1111111l1l_opy_(
                ref,
                f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥႹ"), datetime.now() - bstack1lll11l111_opy_)
            f.bstack11111111ll_opy_(instance, bstack1lllllll1l1_opy_.bstack111111l1ll_opy_, r.success)
    def bstack111111111l_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllllll1l1_opy_.bstack1111111111_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llll1l11l1_opy_.session_id(driver)
        hub_url = bstack1llll1l11l1_opy_.hub_url(driver)
        bstack1lll11l111_opy_ = datetime.now()
        r = self.bstack1lllll11lll_opy_(
            ref,
            f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥႺ"), datetime.now() - bstack1lll11l111_opy_)
        f.bstack11111111ll_opy_(instance, bstack1lllllll1l1_opy_.bstack1111111111_opy_, r.success)
    @measure(event_name=EVENTS.bstack111l111111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1lllll11l1l_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11111_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦႻ") + str(req) + bstack11111_opy_ (u"ࠢࠣႼ"))
        try:
            r = self.bstack1llll1lll11_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦႽ") + str(r.success) + bstack11111_opy_ (u"ࠤࠥႾ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣႿ") + str(e) + bstack11111_opy_ (u"ࠦࠧჀ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll1l111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1lllll1l1ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11111_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢჁ") + str(req) + bstack11111_opy_ (u"ࠨࠢჂ"))
        try:
            r = self.bstack1llll1lll11_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥჃ") + str(r.success) + bstack11111_opy_ (u"ࠣࠤჄ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢჅ") + str(e) + bstack11111_opy_ (u"ࠥࠦ჆"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1lllll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1111111l1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11111_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸ࠿ࠦࠢჇ") + str(req) + bstack11111_opy_ (u"ࠧࠨ჈"))
        try:
            r = self.bstack1llll1lll11_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣ჉") + str(r) + bstack11111_opy_ (u"ࠢࠣ჊"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ჋") + str(e) + bstack11111_opy_ (u"ࠤࠥ჌"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllllll11_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1lllll11lll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11111_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲ࠽ࠤࠧჍ") + str(req) + bstack11111_opy_ (u"ࠦࠧ჎"))
        try:
            r = self.bstack1llll1lll11_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11111_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢ჏") + str(r) + bstack11111_opy_ (u"ࠨࠢა"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧბ") + str(e) + bstack11111_opy_ (u"ࠣࠤგ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11llll1ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1llllllllll_opy_(self, instance: bstack1llll1l1l11_opy_, url: str, f: bstack1llll1l11l1_opy_, kwargs):
        bstack1lllll11l11_opy_ = version.parse(f.framework_version)
        bstack1llllll111l_opy_ = kwargs.get(bstack11111_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥდ"))
        bstack111111l111_opy_ = kwargs.get(bstack11111_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥე"))
        bstack1lllll1ll1l_opy_ = {}
        bstack1lllll11ll1_opy_ = {}
        bstack1lllll1ll11_opy_ = None
        bstack1llll1l1l1l_opy_ = {}
        if bstack111111l111_opy_ is not None or bstack1llllll111l_opy_ is not None: # check top level caps
            if bstack111111l111_opy_ is not None:
                bstack1llll1l1l1l_opy_[bstack11111_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫვ")] = bstack111111l111_opy_
            if bstack1llllll111l_opy_ is not None and callable(getattr(bstack1llllll111l_opy_, bstack11111_opy_ (u"ࠧࡺ࡯ࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢზ"))):
                bstack1llll1l1l1l_opy_[bstack11111_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡢࡵࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩთ")] = bstack1llllll111l_opy_.to_capabilities()
        response = self.bstack1lllll11l1l_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1llll1l1l1l_opy_).encode(bstack11111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨი")))
        if response is not None and response.capabilities:
            bstack1lllll1ll1l_opy_ = json.loads(response.capabilities.decode(bstack11111_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢკ")))
            if not bstack1lllll1ll1l_opy_: # empty caps bstack1lllllll111_opy_ bstack1llll1llll1_opy_ bstack1llll1lll1l_opy_ bstack1llll1ll1ll_opy_ or error in processing
                return
            bstack1lllll1ll11_opy_ = f.bstack1llll1l1ll1_opy_[bstack11111_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨლ")](bstack1lllll1ll1l_opy_)
        if bstack1llllll111l_opy_ is not None and bstack1lllll11l11_opy_ >= version.parse(bstack11111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩმ")):
            bstack1lllll11ll1_opy_ = None
        if (
                not bstack1llllll111l_opy_ and not bstack111111l111_opy_
        ) or (
                bstack1lllll11l11_opy_ < version.parse(bstack11111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪნ"))
        ):
            bstack1lllll11ll1_opy_ = {}
            bstack1lllll11ll1_opy_.update(bstack1lllll1ll1l_opy_)
        self.logger.info(bstack1ll1lllll_opy_)
        if os.environ.get(bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣო")).lower().__eq__(bstack11111_opy_ (u"ࠨࡴࡳࡷࡨࠦპ")):
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥჟ"): f.bstack1llll1ll1l1_opy_,
                }
            )
        if bstack1lllll11l11_opy_ >= version.parse(bstack11111_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨრ")):
            if bstack111111l111_opy_ is not None:
                del kwargs[bstack11111_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤს")]
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦტ"): bstack1lllll1ll11_opy_,
                    bstack11111_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣუ"): True,
                    bstack11111_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧფ"): None,
                }
            )
        elif bstack1lllll11l11_opy_ >= version.parse(bstack11111_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬქ")):
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢღ"): bstack1lllll11ll1_opy_,
                    bstack11111_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤყ"): bstack1lllll1ll11_opy_,
                    bstack11111_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨშ"): True,
                    bstack11111_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥჩ"): None,
                }
            )
        elif bstack1lllll11l11_opy_ >= version.parse(bstack11111_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫც")):
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧძ"): bstack1lllll11ll1_opy_,
                    bstack11111_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥწ"): True,
                    bstack11111_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢჭ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11111_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣხ"): bstack1lllll11ll1_opy_,
                    bstack11111_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨჯ"): True,
                    bstack11111_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥჰ"): None,
                }
            )