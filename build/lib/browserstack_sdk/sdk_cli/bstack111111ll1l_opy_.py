# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack111111l111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1l1ll111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
class bstack11111111l1_opy_(bstack1llll1llll1_opy_):
    bstack1lllll1l1ll_opy_ = bstack1l_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࠨႭ")
    bstack1111111lll_opy_ = bstack1l_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣႮ")
    bstack111111l11l_opy_ = bstack1l_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣႯ")
    def __init__(self, bstack1lllllll111_opy_):
        super().__init__()
        bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1llllll1l1l_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack111111111l_opy_)
        bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1111111111_opy_)
        bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.POST), self.bstack111111l1l1_opy_)
        bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.POST), self.bstack1lllllll11l_opy_)
        bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.QUIT, bstack1llllll1ll1_opy_.POST), self.bstack1llll1ll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack111111111l_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦႰ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨႱ")), str):
                    url = kwargs.get(bstack1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢႲ"))
                elif hasattr(kwargs.get(bstack1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣႳ")), bstack1l_opy_ (u"࠭࡟ࡤ࡮࡬ࡩࡳࡺ࡟ࡤࡱࡱࡪ࡮࡭ࠧႴ")):
                    url = kwargs.get(bstack1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥႵ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦႶ"))._url
            except Exception as e:
                url = bstack1l_opy_ (u"ࠩࠪႷ")
                self.logger.error(bstack1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡸࡶࡱࠦࡦࡳࡱࡰࠤࡩࡸࡩࡷࡧࡵ࠾ࠥࢁࡽࠣႸ").format(e))
            self.logger.info(bstack1l_opy_ (u"ࠦࡗ࡫࡭ࡰࡶࡨࠤࡘ࡫ࡲࡷࡧࡵࠤࡆࡪࡤࡳࡧࡶࡷࠥࡨࡥࡪࡰࡪࠤࡵࡧࡳࡴࡧࡧࠤࡦࡹࠠ࠻ࠢࡾࢁࠧႹ").format(str(url)))
            self.bstack1lllll11111_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1l_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠳ࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࡻࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࡾ࠼ࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥႺ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1111111111_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack11111111l1_opy_.bstack1lllll1l1ll_opy_, False):
            return
        if not f.bstack1llllllll11_opy_(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_)
        if f.bstack1lllll1llll_opy_(method_name, *args) and len(args) > 1:
            bstack1l1111lll_opy_ = datetime.now()
            hub_url = bstack1lllll1ll1l_opy_.hub_url(driver)
            self.logger.warning(bstack1l_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲ࠽ࠣႻ") + str(hub_url) + bstack1l_opy_ (u"ࠢࠣႼ"))
            bstack111111ll11_opy_ = args[1][bstack1l_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢႽ")] if isinstance(args[1], dict) and bstack1l_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣႾ") in args[1] else None
            bstack1lllll11lll_opy_ = bstack1l_opy_ (u"ࠥࡥࡱࡽࡡࡺࡵࡐࡥࡹࡩࡨࠣႿ")
            if isinstance(bstack111111ll11_opy_, dict):
                bstack1l1111lll_opy_ = datetime.now()
                r = self.bstack111111l1ll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤჀ"), datetime.now() - bstack1l1111lll_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1l_opy_ (u"ࠧࡹ࡯࡮ࡧࡷ࡬࡮ࡴࡧࠡࡹࡨࡲࡹࠦࡷࡳࡱࡱ࡫࠿ࠦࠢჁ") + str(r) + bstack1l_opy_ (u"ࠨࠢჂ"))
                        return
                    if r.hub_url:
                        f.bstack1lllll11l11_opy_(instance, driver, r.hub_url)
                        f.bstack1lllll11ll1_opy_(instance, bstack11111111l1_opy_.bstack1lllll1l1ll_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨჃ"), e)
    def bstack111111l1l1_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll1ll1l_opy_.session_id(driver)
            if session_id:
                bstack1llllll11ll_opy_ = bstack1l_opy_ (u"ࠣࡽࢀ࠾ࡸࡺࡡࡳࡶࠥჄ").format(session_id)
                bstack1llll1l1lll_opy_.mark(bstack1llllll11ll_opy_)
    def bstack1lllllll11l_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack11111111l1_opy_.bstack1111111lll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll1ll1l_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡭ࡻࡢࡠࡷࡵࡰࡂࠨჅ") + str(hub_url) + bstack1l_opy_ (u"ࠥࠦ჆"))
            return
        framework_session_id = bstack1lllll1ll1l_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢჇ") + str(framework_session_id) + bstack1l_opy_ (u"ࠧࠨ჈"))
            return
        if bstack1lllll1ll1l_opy_.bstack1llllll111l_opy_(*args) == bstack1lllll1ll1l_opy_.bstack1llllllll1l_opy_:
            bstack1llllll11l1_opy_ = bstack1l_opy_ (u"ࠨࡻࡾ࠼ࡨࡲࡩࠨ჉").format(framework_session_id)
            bstack1llllll11ll_opy_ = bstack1l_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤ჊").format(framework_session_id)
            bstack1llll1l1lll_opy_.end(
                label=bstack1l_opy_ (u"ࠣࡵࡧ࡯࠿ࡪࡲࡪࡸࡨࡶ࠿ࡶ࡯ࡴࡶ࠰࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿࡧࡴࡪࡱࡱࠦ჋"),
                start=bstack1llllll11ll_opy_,
                end=bstack1llllll11l1_opy_,
                status=True,
                failure=None
            )
            bstack1l1111lll_opy_ = datetime.now()
            r = self.bstack1llllll1l11_opy_(
                ref,
                f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴࠣ჌"), datetime.now() - bstack1l1111lll_opy_)
            f.bstack1lllll11ll1_opy_(instance, bstack11111111l1_opy_.bstack1111111lll_opy_, r.success)
    def bstack1llll1ll1ll_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack11111111l1_opy_.bstack111111l11l_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll1ll1l_opy_.session_id(driver)
        hub_url = bstack1lllll1ll1l_opy_.hub_url(driver)
        bstack1l1111lll_opy_ = datetime.now()
        r = self.bstack1lllllll1ll_opy_(
            ref,
            f.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰࠣჍ"), datetime.now() - bstack1l1111lll_opy_)
        f.bstack1lllll11ll1_opy_(instance, bstack11111111l1_opy_.bstack111111l11l_opy_, r.success)
    @measure(event_name=EVENTS.bstack1lll1ll111_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1lllll111l1_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡷࡦࡤࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤ჎") + str(req) + bstack1l_opy_ (u"ࠧࠨ჏"))
        try:
            r = self.bstack1llll1lll1l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤა") + str(r.success) + bstack1l_opy_ (u"ࠢࠣბ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨგ") + str(e) + bstack1l_opy_ (u"ࠤࠥდ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1ll1l1_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack111111l1ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧე") + str(req) + bstack1l_opy_ (u"ࠦࠧვ"))
        try:
            r = self.bstack1llll1lll1l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣზ") + str(r.success) + bstack1l_opy_ (u"ࠨࠢთ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧი") + str(e) + bstack1l_opy_ (u"ࠣࠤკ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11111111ll_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1llllll1l11_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶ࠽ࠤࠧლ") + str(req) + bstack1l_opy_ (u"ࠥࠦმ"))
        try:
            r = self.bstack1llll1lll1l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨნ") + str(r) + bstack1l_opy_ (u"ࠧࠨო"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦპ") + str(e) + bstack1l_opy_ (u"ࠢࠣჟ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1l1ll1_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1lllllll1ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡵࡰ࠻ࠢࠥრ") + str(req) + bstack1l_opy_ (u"ࠤࠥს"))
        try:
            r = self.bstack1llll1lll1l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1l_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧტ") + str(r) + bstack1l_opy_ (u"ࠦࠧუ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥფ") + str(e) + bstack1l_opy_ (u"ࠨࠢქ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllllll1_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1lllll11111_opy_(self, instance: bstack111111l111_opy_, url: str, f: bstack1lllll1ll1l_opy_, kwargs):
        bstack1llll1ll11l_opy_ = version.parse(f.framework_version)
        bstack111111lll1_opy_ = kwargs.get(bstack1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣღ"))
        bstack1llll1l1l1l_opy_ = kwargs.get(bstack1l_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣყ"))
        bstack1llll1ll111_opy_ = {}
        bstack1lllllll1l1_opy_ = {}
        bstack1llllll1lll_opy_ = None
        bstack1lllll11l1l_opy_ = {}
        if bstack1llll1l1l1l_opy_ is not None or bstack111111lll1_opy_ is not None: # check top level caps
            if bstack1llll1l1l1l_opy_ is not None:
                bstack1lllll11l1l_opy_[bstack1l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩშ")] = bstack1llll1l1l1l_opy_
            if bstack111111lll1_opy_ is not None and callable(getattr(bstack111111lll1_opy_, bstack1l_opy_ (u"ࠥࡸࡴࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧჩ"))):
                bstack1lllll11l1l_opy_[bstack1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࡤࡧࡳࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧც")] = bstack111111lll1_opy_.to_capabilities()
        response = self.bstack1lllll111l1_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll11l1l_opy_).encode(bstack1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦძ")))
        if response is not None and response.capabilities:
            bstack1llll1ll111_opy_ = json.loads(response.capabilities.decode(bstack1l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧწ")))
            if not bstack1llll1ll111_opy_: # empty caps bstack1llllllllll_opy_ bstack1lllll111ll_opy_ bstack1lllllllll1_opy_ bstack1llllll1111_opy_ or error in processing
                return
            bstack1llllll1lll_opy_ = f.bstack1lllll1lll1_opy_[bstack1l_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࡠࡨࡵࡳࡲࡥࡣࡢࡲࡶࠦჭ")](bstack1llll1ll111_opy_)
        if bstack111111lll1_opy_ is not None and bstack1llll1ll11l_opy_ >= version.parse(bstack1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧხ")):
            bstack1lllllll1l1_opy_ = None
        if (
                not bstack111111lll1_opy_ and not bstack1llll1l1l1l_opy_
        ) or (
                bstack1llll1ll11l_opy_ < version.parse(bstack1l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨჯ"))
        ):
            bstack1lllllll1l1_opy_ = {}
            bstack1lllllll1l1_opy_.update(bstack1llll1ll111_opy_)
        self.logger.info(bstack1l1l1ll111_opy_)
        if os.environ.get(bstack1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓࠨჰ")).lower().__eq__(bstack1l_opy_ (u"ࠦࡹࡸࡵࡦࠤჱ")):
            kwargs.update(
                {
                    bstack1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣჲ"): f.bstack1lllll1l1l1_opy_,
                }
            )
        if bstack1llll1ll11l_opy_ >= version.parse(bstack1l_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ჳ")):
            if bstack1llll1l1l1l_opy_ is not None:
                del kwargs[bstack1l_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢჴ")]
            kwargs.update(
                {
                    bstack1l_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤჵ"): bstack1llllll1lll_opy_,
                    bstack1l_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨჶ"): True,
                    bstack1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥჷ"): None,
                }
            )
        elif bstack1llll1ll11l_opy_ >= version.parse(bstack1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪჸ")):
            kwargs.update(
                {
                    bstack1l_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧჹ"): bstack1lllllll1l1_opy_,
                    bstack1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢჺ"): bstack1llllll1lll_opy_,
                    bstack1l_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦ჻"): True,
                    bstack1l_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣჼ"): None,
                }
            )
        elif bstack1llll1ll11l_opy_ >= version.parse(bstack1l_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩჽ")):
            kwargs.update(
                {
                    bstack1l_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥჾ"): bstack1lllllll1l1_opy_,
                    bstack1l_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣჿ"): True,
                    bstack1l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᄀ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1l_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄁ"): bstack1lllllll1l1_opy_,
                    bstack1l_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᄂ"): True,
                    bstack1l_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᄃ"): None,
                }
            )