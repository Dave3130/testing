# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1llllllll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1lllll1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
class bstack1lllll1ll1l_opy_(bstack1111111ll1_opy_):
    bstack1llllllll11_opy_ = bstack1l1lll1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࠨႦ")
    bstack1lllll11ll1_opy_ = bstack1l1lll1_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣႧ")
    bstack1lllllll1l1_opy_ = bstack1l1lll1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣႨ")
    def __init__(self, bstack1llll1l1lll_opy_):
        super().__init__()
        bstack1lllll111l1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1lllll1l11l_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1lllll1lll1_opy_)
        bstack1lllll111l1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1111111111_opy_)
        bstack1lllll111l1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.POST), self.bstack1llllll1l1l_opy_)
        bstack1lllll111l1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.POST), self.bstack1lllll11lll_opy_)
        bstack1lllll111l1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.QUIT, bstack1llll1ll111_opy_.POST), self.bstack1llllll11l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1lll1_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1lll1_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦႩ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1l1lll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨႪ")), str):
                    url = kwargs.get(bstack1l1lll1_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢႫ"))
                elif hasattr(kwargs.get(bstack1l1lll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣႬ")), bstack1l1lll1_opy_ (u"࠭࡟ࡤ࡮࡬ࡩࡳࡺ࡟ࡤࡱࡱࡪ࡮࡭ࠧႭ")):
                    url = kwargs.get(bstack1l1lll1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥႮ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1l1lll1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦႯ"))._url
            except Exception as e:
                url = bstack1l1lll1_opy_ (u"ࠩࠪႰ")
                self.logger.error(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡸࡶࡱࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠾ࠥࢁࡽࠣႱ").format(e))
            self.logger.info(bstack1l1lll1_opy_ (u"ࠦࡗ࡫࡭ࡰࡶࡨࠤࡘ࡫ࡲࡷࡧࡵࠤࡆࡪࡤࡳࡧࡶࡷࠥࡨࡥࡪࡰࡪࠤࡵࡧࡳࡴࡧࡧࠤࡦࡹࠠ࠻ࠢࡾࢁࠧႲ").format(str(url)))
            self.bstack1lllllll1ll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1l1lll1_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠳ࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾ࠼ࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥႳ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1111111111_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llllllll11_opy_, False):
            return
        if not f.bstack1llllll111l_opy_(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_)
        if f.bstack1111111l1l_opy_(method_name, *args) and len(args) > 1:
            bstack11ll11ll1_opy_ = datetime.now()
            hub_url = bstack1lllll111l1_opy_.hub_url(driver)
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲ࠽ࠣႴ") + str(hub_url) + bstack1l1lll1_opy_ (u"ࠢࠣႵ"))
            bstack1llll1ll1ll_opy_ = args[1][bstack1l1lll1_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢႶ")] if isinstance(args[1], dict) and bstack1l1lll1_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣႷ") in args[1] else None
            bstack111111111l_opy_ = bstack1l1lll1_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣႸ")
            if isinstance(bstack1llll1ll1ll_opy_, dict):
                bstack11ll11ll1_opy_ = datetime.now()
                r = self.bstack1llllll1l11_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤႹ"), datetime.now() - bstack11ll11ll1_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1l1lll1_opy_ (u"ࠧࡹ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫࠿ࠦࠢႺ") + str(r) + bstack1l1lll1_opy_ (u"ࠨࠢႻ"))
                        return
                    if r.hub_url:
                        f.bstack111111l1ll_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1lllll_opy_(instance, bstack1lllll1ll1l_opy_.bstack1llllllll11_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨႼ"), e)
    def bstack1llllll1l1l_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll111l1_opy_.session_id(driver)
            if session_id:
                bstack1llll1l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠣࡽࢀ࠾ࡸࡺࡡࡳࡶࠥႽ").format(session_id)
                bstack1llll1ll11l_opy_.mark(bstack1llll1l1l11_opy_)
    def bstack1lllll11lll_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1lllll11ll1_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll111l1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡭ࡻࡢࡠࡷࡵࡰࡂࠨႾ") + str(hub_url) + bstack1l1lll1_opy_ (u"ࠥࠦႿ"))
            return
        framework_session_id = bstack1lllll111l1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢჀ") + str(framework_session_id) + bstack1l1lll1_opy_ (u"ࠧࠨჁ"))
            return
        if bstack1lllll111l1_opy_.bstack1lllll11111_opy_(*args) == bstack1lllll111l1_opy_.bstack1llll1l11ll_opy_:
            bstack1lllll1l111_opy_ = bstack1l1lll1_opy_ (u"ࠨࡻࡾ࠼ࡨࡲࡩࠨჂ").format(framework_session_id)
            bstack1llll1l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤჃ").format(framework_session_id)
            bstack1llll1ll11l_opy_.end(
                label=bstack1l1lll1_opy_ (u"ࠣࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶ࡯ࡴࡶ࠰࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠦჄ"),
                start=bstack1llll1l1l11_opy_,
                end=bstack1lllll1l111_opy_,
                status=True,
                failure=None
            )
            bstack11ll11ll1_opy_ = datetime.now()
            r = self.bstack111111l1l1_opy_(
                ref,
                f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣჅ"), datetime.now() - bstack11ll11ll1_opy_)
            f.bstack1llll1lllll_opy_(instance, bstack1lllll1ll1l_opy_.bstack1lllll11ll1_opy_, r.success)
    def bstack1llllll11l1_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1lllllll1l1_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll111l1_opy_.session_id(driver)
        hub_url = bstack1lllll111l1_opy_.hub_url(driver)
        bstack11ll11ll1_opy_ = datetime.now()
        r = self.bstack1llllll11ll_opy_(
            ref,
            f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1ll1_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣ჆"), datetime.now() - bstack11ll11ll1_opy_)
        f.bstack1llll1lllll_opy_(instance, bstack1lllll1ll1l_opy_.bstack1lllllll1l1_opy_, r.success)
    @measure(event_name=EVENTS.bstack1ll1ll1111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1llllll1lll_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤჇ") + str(req) + bstack1l1lll1_opy_ (u"ࠧࠨ჈"))
        try:
            r = self.bstack1lllll1ll11_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤ჉") + str(r.success) + bstack1l1lll1_opy_ (u"ࠢࠣ჊"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ჋") + str(e) + bstack1l1lll1_opy_ (u"ࠤࠥ჌"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll1111l_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1llllll1l11_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llll1llll1_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧჍ") + str(req) + bstack1l1lll1_opy_ (u"ࠦࠧ჎"))
        try:
            r = self.bstack1lllll1ll11_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣ჏") + str(r.success) + bstack1l1lll1_opy_ (u"ࠨࠢა"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧბ") + str(e) + bstack1l1lll1_opy_ (u"ࠣࠤგ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll1ll1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack111111l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1llll1_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶ࠽ࠤࠧდ") + str(req) + bstack1l1lll1_opy_ (u"ࠥࠦე"))
        try:
            r = self.bstack1lllll1ll11_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨვ") + str(r) + bstack1l1lll1_opy_ (u"ࠧࠨზ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦთ") + str(e) + bstack1l1lll1_opy_ (u"ࠢࠣი"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll111ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1llllll11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1llll1_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰ࠻ࠢࠥკ") + str(req) + bstack1l1lll1_opy_ (u"ࠤࠥლ"))
        try:
            r = self.bstack1lllll1ll11_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧმ") + str(r) + bstack1l1lll1_opy_ (u"ࠦࠧნ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥო") + str(e) + bstack1l1lll1_opy_ (u"ࠨࠢპ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1lllll11_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1lllllll1ll_opy_(self, instance: bstack1llllllll1l_opy_, url: str, f: bstack1lllll111l1_opy_, kwargs):
        bstack1llll1lll1l_opy_ = version.parse(f.framework_version)
        bstack11111111ll_opy_ = kwargs.get(bstack1l1lll1_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣჟ"))
        bstack1111111l11_opy_ = kwargs.get(bstack1l1lll1_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣრ"))
        bstack1llll1l1l1l_opy_ = {}
        bstack1lllll1l1ll_opy_ = {}
        bstack1llll1ll1l1_opy_ = None
        bstack1lllll11l1l_opy_ = {}
        if bstack1111111l11_opy_ is not None or bstack11111111ll_opy_ is not None: # check top level caps
            if bstack1111111l11_opy_ is not None:
                bstack1lllll11l1l_opy_[bstack1l1lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩს")] = bstack1111111l11_opy_
            if bstack11111111ll_opy_ is not None and callable(getattr(bstack11111111ll_opy_, bstack1l1lll1_opy_ (u"ࠥࡸࡴࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧტ"))):
                bstack1lllll11l1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࡤࡧࡳࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧუ")] = bstack11111111ll_opy_.to_capabilities()
        response = self.bstack1llllll1lll_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll11l1l_opy_).encode(bstack1l1lll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦფ")))
        if response is not None and response.capabilities:
            bstack1llll1l1l1l_opy_ = json.loads(response.capabilities.decode(bstack1l1lll1_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧქ")))
            if not bstack1llll1l1l1l_opy_: # empty caps bstack1lllll11l11_opy_ bstack111111l111_opy_ bstack1lllllll111_opy_ bstack1lllll1l1l1_opy_ or error in processing
                return
            bstack1llll1ll1l1_opy_ = f.bstack1lllllll11l_opy_[bstack1l1lll1_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࡠࡨࡵࡳࡲࡥࡣࡢࡲࡶࠦღ")](bstack1llll1l1l1l_opy_)
        if bstack11111111ll_opy_ is not None and bstack1llll1lll1l_opy_ >= version.parse(bstack1l1lll1_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧყ")):
            bstack1lllll1l1ll_opy_ = None
        if (
                not bstack11111111ll_opy_ and not bstack1111111l11_opy_
        ) or (
                bstack1llll1lll1l_opy_ < version.parse(bstack1l1lll1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨშ"))
        ):
            bstack1lllll1l1ll_opy_ = {}
            bstack1lllll1l1ll_opy_.update(bstack1llll1l1l1l_opy_)
        self.logger.info(bstack1lllll1lll_opy_)
        if os.environ.get(bstack1l1lll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨჩ")).lower().__eq__(bstack1l1lll1_opy_ (u"ࠦࡹࡸࡵࡦࠤც")):
            kwargs.update(
                {
                    bstack1l1lll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣძ"): f.bstack1111111lll_opy_,
                }
            )
        if bstack1llll1lll1l_opy_ >= version.parse(bstack1l1lll1_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭წ")):
            if bstack1111111l11_opy_ is not None:
                del kwargs[bstack1l1lll1_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢჭ")]
            kwargs.update(
                {
                    bstack1l1lll1_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤხ"): bstack1llll1ll1l1_opy_,
                    bstack1l1lll1_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨჯ"): True,
                    bstack1l1lll1_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥჰ"): None,
                }
            )
        elif bstack1llll1lll1l_opy_ >= version.parse(bstack1l1lll1_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪჱ")):
            kwargs.update(
                {
                    bstack1l1lll1_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧჲ"): bstack1lllll1l1ll_opy_,
                    bstack1l1lll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢჳ"): bstack1llll1ll1l1_opy_,
                    bstack1l1lll1_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦჴ"): True,
                    bstack1l1lll1_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣჵ"): None,
                }
            )
        elif bstack1llll1lll1l_opy_ >= version.parse(bstack1l1lll1_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩჶ")):
            kwargs.update(
                {
                    bstack1l1lll1_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥჷ"): bstack1lllll1l1ll_opy_,
                    bstack1l1lll1_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣჸ"): True,
                    bstack1l1lll1_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧჹ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1l1lll1_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨჺ"): bstack1lllll1l1ll_opy_,
                    bstack1l1lll1_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦ჻"): True,
                    bstack1l1lll1_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣჼ"): None,
                }
            )