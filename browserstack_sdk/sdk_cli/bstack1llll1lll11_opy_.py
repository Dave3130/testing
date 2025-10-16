# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll1111_opy_ import bstack111111ll11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1lllllll1ll_opy_,
    bstack111111111l_opy_,
    bstack111111lll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import bstack1lllll11ll1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1111llll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
class bstack111111l1ll_opy_(bstack111111ll11_opy_):
    bstack1lllll1l1ll_opy_ = bstack1ll11_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶࠥႪ")
    bstack1lllll11l1l_opy_ = bstack1ll11_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸࠧႫ")
    bstack1llll1l1lll_opy_ = bstack1ll11_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴࠧႬ")
    def __init__(self, bstack1lllllll111_opy_):
        super().__init__()
        bstack1lllll11ll1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1lllllll1l1_opy_, bstack111111111l_opy_.PRE), self.bstack1llll1llll1_opy_)
        bstack1lllll11ll1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_, bstack111111111l_opy_.PRE), self.bstack1llllll1lll_opy_)
        bstack1lllll11ll1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_, bstack111111111l_opy_.POST), self.bstack111111ll1l_opy_)
        bstack1lllll11ll1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.bstack1llllll11ll_opy_, bstack111111111l_opy_.POST), self.bstack11111111ll_opy_)
        bstack1lllll11ll1_opy_.bstack11111111l1_opy_((bstack1lllllll1ll_opy_.QUIT, bstack111111111l_opy_.POST), self.bstack1111111ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1llll1_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll11_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣႭ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1ll11_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥႮ")), str):
                    url = kwargs.get(bstack1ll11_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦႯ"))
                elif hasattr(kwargs.get(bstack1ll11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧႰ")), bstack1ll11_opy_ (u"ࠪࡣࡨࡲࡩࡦࡰࡷࡣࡨࡵ࡮ࡧ࡫ࡪࠫႱ")):
                    url = kwargs.get(bstack1ll11_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢႲ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1ll11_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣႳ"))._url
            except Exception as e:
                url = bstack1ll11_opy_ (u"࠭ࠧႴ")
                self.logger.error(bstack1ll11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡵࡳ࡮ࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࢁࠧႵ").format(e))
            self.logger.info(bstack1ll11_opy_ (u"ࠣࡔࡨࡱࡴࡺࡥࠡࡕࡨࡶࡻ࡫ࡲࠡࡃࡧࡨࡷ࡫ࡳࡴࠢࡥࡩ࡮ࡴࡧࠡࡲࡤࡷࡸ࡫ࡤࠡࡣࡶࠤ࠿ࠦࡻࡾࠤႶ").format(str(url)))
            self.bstack1llllll1l11_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1ll11_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࡿࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࢂࡀࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢႷ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1llllll1lll_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack111111l1ll_opy_.bstack1lllll1l1ll_opy_, False):
            return
        if not f.bstack1111111lll_opy_(instance, bstack1lllll11ll1_opy_.bstack1lllll111ll_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll11ll1_opy_.bstack1lllll111ll_opy_)
        if f.bstack1lllll111l1_opy_(method_name, *args) and len(args) > 1:
            bstack11l1lll1l_opy_ = datetime.now()
            hub_url = bstack1lllll11ll1_opy_.hub_url(driver)
            self.logger.warning(bstack1ll11_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧႸ") + str(hub_url) + bstack1ll11_opy_ (u"ࠦࠧႹ"))
            bstack1lllll1ll1l_opy_ = args[1][bstack1ll11_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦႺ")] if isinstance(args[1], dict) and bstack1ll11_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧႻ") in args[1] else None
            bstack1llll1ll1l1_opy_ = bstack1ll11_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧႼ")
            if isinstance(bstack1lllll1ll1l_opy_, dict):
                bstack11l1lll1l_opy_ = datetime.now()
                r = self.bstack1lllllllll1_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࠨႽ"), datetime.now() - bstack11l1lll1l_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1ll11_opy_ (u"ࠤࡶࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨ࠼ࠣࠦႾ") + str(r) + bstack1ll11_opy_ (u"ࠥࠦႿ"))
                        return
                    if r.hub_url:
                        f.bstack111111l1l1_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1ll1ll_opy_(instance, bstack111111l1ll_opy_.bstack1lllll1l1ll_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1ll11_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥჀ"), e)
    def bstack111111ll1l_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll11ll1_opy_.session_id(driver)
            if session_id:
                bstack111111l111_opy_ = bstack1ll11_opy_ (u"ࠧࢁࡽ࠻ࡵࡷࡥࡷࡺࠢჁ").format(session_id)
                bstack1llll1lllll_opy_.mark(bstack111111l111_opy_)
    def bstack11111111ll_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack111111l1ll_opy_.bstack1lllll11l1l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll11ll1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1ll11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥჂ") + str(hub_url) + bstack1ll11_opy_ (u"ࠢࠣჃ"))
            return
        framework_session_id = bstack1lllll11ll1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1ll11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦჄ") + str(framework_session_id) + bstack1ll11_opy_ (u"ࠤࠥჅ"))
            return
        if bstack1lllll11ll1_opy_.bstack1lllll1ll11_opy_(*args) == bstack1lllll11ll1_opy_.bstack1llllll1ll1_opy_:
            bstack1lllll11l11_opy_ = bstack1ll11_opy_ (u"ࠥࡿࢂࡀࡥ࡯ࡦࠥ჆").format(framework_session_id)
            bstack111111l111_opy_ = bstack1ll11_opy_ (u"ࠦࢀࢃ࠺ࡴࡶࡤࡶࡹࠨჇ").format(framework_session_id)
            bstack1llll1lllll_opy_.end(
                label=bstack1ll11_opy_ (u"ࠧࡹࡤ࡬࠼ࡧࡶ࡮ࡼࡥࡳ࠼ࡳࡳࡸࡺ࠭ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠣ჈"),
                start=bstack111111l111_opy_,
                end=bstack1lllll11l11_opy_,
                status=True,
                failure=None
            )
            bstack11l1lll1l_opy_ = datetime.now()
            r = self.bstack1llll1l1l1l_opy_(
                ref,
                f.get_state(instance, bstack1lllll11ll1_opy_.bstack1lllll111ll_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸࠧ჉"), datetime.now() - bstack11l1lll1l_opy_)
            f.bstack1llll1ll1ll_opy_(instance, bstack111111l1ll_opy_.bstack1lllll11l1l_opy_, r.success)
    def bstack1111111ll1_opy_(
        self,
        f: bstack1lllll11ll1_opy_,
        driver: object,
        exec: Tuple[bstack111111lll1_opy_, str],
        bstack1llll1l1ll1_opy_: Tuple[bstack1lllllll1ll_opy_, bstack111111111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack111111l1ll_opy_.bstack1llll1l1lll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll11ll1_opy_.session_id(driver)
        hub_url = bstack1lllll11ll1_opy_.hub_url(driver)
        bstack11l1lll1l_opy_ = datetime.now()
        r = self.bstack1lllll1l1l1_opy_(
            ref,
            f.get_state(instance, bstack1lllll11ll1_opy_.bstack1lllll111ll_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴࠧ჊"), datetime.now() - bstack11l1lll1l_opy_)
        f.bstack1llll1ll1ll_opy_(instance, bstack111111l1ll_opy_.bstack1llll1l1lll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1ll1l11l1l_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1111111111_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1ll11_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨ჋") + str(req) + bstack1ll11_opy_ (u"ࠤࠥ჌"))
        try:
            r = self.bstack1llllll111l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1ll11_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨჍ") + str(r.success) + bstack1ll11_opy_ (u"ࠦࠧ჎"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥ჏") + str(e) + bstack1ll11_opy_ (u"ࠨࠢა"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllllllll_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1lllllllll1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1111111l1l_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1ll11_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤბ") + str(req) + bstack1ll11_opy_ (u"ࠣࠤგ"))
        try:
            r = self.bstack1llllll111l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1ll11_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࡷࡺࡩࡣࡦࡵࡶࡁࠧდ") + str(r.success) + bstack1ll11_opy_ (u"ࠥࠦე"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤვ") + str(e) + bstack1ll11_opy_ (u"ࠧࠨზ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11lll_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1llll1l1l1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1111111l1l_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1ll11_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺ࠺ࠡࠤთ") + str(req) + bstack1ll11_opy_ (u"ࠢࠣი"))
        try:
            r = self.bstack1llllll111l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1ll11_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥკ") + str(r) + bstack1ll11_opy_ (u"ࠤࠥლ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣმ") + str(e) + bstack1ll11_opy_ (u"ࠦࠧნ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllllll11_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1lllll1l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1111111l1l_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1ll11_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴ࠿ࠦࠢო") + str(req) + bstack1ll11_opy_ (u"ࠨࠢპ"))
        try:
            r = self.bstack1llllll111l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1ll11_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤჟ") + str(r) + bstack1ll11_opy_ (u"ࠣࠤრ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢს") + str(e) + bstack1ll11_opy_ (u"ࠥࠦტ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll1l1ll1_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1llllll1l11_opy_(self, instance: bstack111111lll1_opy_, url: str, f: bstack1lllll11ll1_opy_, kwargs):
        bstack1llllll11l1_opy_ = version.parse(f.framework_version)
        bstack1llll1ll11l_opy_ = kwargs.get(bstack1ll11_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧუ"))
        bstack1lllll1llll_opy_ = kwargs.get(bstack1ll11_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧფ"))
        bstack1llllllll1l_opy_ = {}
        bstack1lllll1lll1_opy_ = {}
        bstack1lllllll11l_opy_ = None
        bstack1lllll1111l_opy_ = {}
        if bstack1lllll1llll_opy_ is not None or bstack1llll1ll11l_opy_ is not None: # check top level caps
            if bstack1lllll1llll_opy_ is not None:
                bstack1lllll1111l_opy_[bstack1ll11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ქ")] = bstack1lllll1llll_opy_
            if bstack1llll1ll11l_opy_ is not None and callable(getattr(bstack1llll1ll11l_opy_, bstack1ll11_opy_ (u"ࠢࡵࡱࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤღ"))):
                bstack1lllll1111l_opy_[bstack1ll11_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡤࡷࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫყ")] = bstack1llll1ll11l_opy_.to_capabilities()
        response = self.bstack1111111111_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll1111l_opy_).encode(bstack1ll11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣშ")))
        if response is not None and response.capabilities:
            bstack1llllllll1l_opy_ = json.loads(response.capabilities.decode(bstack1ll11_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤჩ")))
            if not bstack1llllllll1l_opy_: # empty caps bstack1lllll1l11l_opy_ bstack111111l11l_opy_ bstack1lllll1l111_opy_ bstack1lllll11111_opy_ or error in processing
                return
            bstack1lllllll11l_opy_ = f.bstack1111111l11_opy_[bstack1ll11_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡣࡴࡶࡴࡪࡱࡱࡷࡤ࡬ࡲࡰ࡯ࡢࡧࡦࡶࡳࠣც")](bstack1llllllll1l_opy_)
        if bstack1llll1ll11l_opy_ is not None and bstack1llllll11l1_opy_ >= version.parse(bstack1ll11_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫძ")):
            bstack1lllll1lll1_opy_ = None
        if (
                not bstack1llll1ll11l_opy_ and not bstack1lllll1llll_opy_
        ) or (
                bstack1llllll11l1_opy_ < version.parse(bstack1ll11_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬწ"))
        ):
            bstack1lllll1lll1_opy_ = {}
            bstack1lllll1lll1_opy_.update(bstack1llllllll1l_opy_)
        self.logger.info(bstack1111llll1l_opy_)
        if os.environ.get(bstack1ll11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠥჭ")).lower().__eq__(bstack1ll11_opy_ (u"ࠣࡶࡵࡹࡪࠨხ")):
            kwargs.update(
                {
                    bstack1ll11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧჯ"): f.bstack1llll1ll111_opy_,
                }
            )
        if bstack1llllll11l1_opy_ >= version.parse(bstack1ll11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪჰ")):
            if bstack1lllll1llll_opy_ is not None:
                del kwargs[bstack1ll11_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦჱ")]
            kwargs.update(
                {
                    bstack1ll11_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨჲ"): bstack1lllllll11l_opy_,
                    bstack1ll11_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥჳ"): True,
                    bstack1ll11_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢჴ"): None,
                }
            )
        elif bstack1llllll11l1_opy_ >= version.parse(bstack1ll11_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧჵ")):
            kwargs.update(
                {
                    bstack1ll11_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤჶ"): bstack1lllll1lll1_opy_,
                    bstack1ll11_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦჷ"): bstack1lllllll11l_opy_,
                    bstack1ll11_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣჸ"): True,
                    bstack1ll11_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧჹ"): None,
                }
            )
        elif bstack1llllll11l1_opy_ >= version.parse(bstack1ll11_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ჺ")):
            kwargs.update(
                {
                    bstack1ll11_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢ჻"): bstack1lllll1lll1_opy_,
                    bstack1ll11_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧჼ"): True,
                    bstack1ll11_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤჽ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1ll11_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥჾ"): bstack1lllll1lll1_opy_,
                    bstack1ll11_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣჿ"): True,
                    bstack1ll11_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᄀ"): None,
                }
            )