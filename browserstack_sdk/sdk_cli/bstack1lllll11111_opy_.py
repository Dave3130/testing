# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
    bstack1llllllll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll11l11_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1l111l11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
class bstack1llll1l1l1l_opy_(bstack1llll1lll1l_opy_):
    bstack1llllll1111_opy_ = bstack1ll1l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸࠧႥ")
    bstack1llll1ll111_opy_ = bstack1ll1l_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺࠢႦ")
    bstack1lllll111ll_opy_ = bstack1ll1l_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶࠢႧ")
    def __init__(self, bstack111111111l_opy_):
        super().__init__()
        bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1llll1ll11l_opy_, bstack1111111lll_opy_.PRE), self.bstack1llllll1l11_opy_)
        bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.PRE), self.bstack1llllll1ll1_opy_)
        bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.POST), self.bstack1llllllll11_opy_)
        bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.POST), self.bstack1lllll1llll_opy_)
        bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.QUIT, bstack1111111lll_opy_.POST), self.bstack1llll1lllll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllll1l11_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1ll1l_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥႨ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1ll1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧႩ")), str):
                    url = kwargs.get(bstack1ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨႪ"))
                elif hasattr(kwargs.get(bstack1ll1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢႫ")), bstack1ll1l_opy_ (u"ࠬࡥࡣ࡭࡫ࡨࡲࡹࡥࡣࡰࡰࡩ࡭࡬࠭Ⴌ")):
                    url = kwargs.get(bstack1ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤႭ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1ll1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥႮ"))._url
            except Exception as e:
                url = bstack1ll1l_opy_ (u"ࠨࠩႯ")
                self.logger.error(bstack1ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡷࡵࡰࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀࢃࠢႰ").format(e))
            self.logger.info(bstack1ll1l_opy_ (u"ࠥࡖࡪࡳ࡯ࡵࡧࠣࡗࡪࡸࡶࡦࡴࠣࡅࡩࡪࡲࡦࡵࡶࠤࡧ࡫ࡩ࡯ࡩࠣࡴࡦࡹࡳࡦࡦࠣࡥࡸࠦ࠺ࠡࡽࢀࠦႱ").format(str(url)))
            self.bstack1llllll11ll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1ll1l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࡽ࠻ࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤႲ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1llllll1ll1_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llll1l1l1l_opy_.bstack1llllll1111_opy_, False):
            return
        if not f.bstack1lllll11lll_opy_(instance, bstack1lllll11l11_opy_.bstack1lllllllll1_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll11l11_opy_.bstack1lllllllll1_opy_)
        if f.bstack1lllll1111l_opy_(method_name, *args) and len(args) > 1:
            bstack1l11l11lll_opy_ = datetime.now()
            hub_url = bstack1lllll11l11_opy_.hub_url(driver)
            self.logger.warning(bstack1ll1l_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࡃࠢႳ") + str(hub_url) + bstack1ll1l_opy_ (u"ࠨࠢႴ"))
            bstack1lllll1ll11_opy_ = args[1][bstack1ll1l_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨႵ")] if isinstance(args[1], dict) and bstack1ll1l_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢႶ") in args[1] else None
            bstack1lllll1lll1_opy_ = bstack1ll1l_opy_ (u"ࠤࡤࡰࡼࡧࡹࡴࡏࡤࡸࡨ࡮ࠢႷ")
            if isinstance(bstack1lllll1ll11_opy_, dict):
                bstack1l11l11lll_opy_ = datetime.now()
                r = self.bstack1lllll1ll1l_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴࠣႸ"), datetime.now() - bstack1l11l11lll_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1ll1l_opy_ (u"ࠦࡸࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪ࠾ࠥࠨႹ") + str(r) + bstack1ll1l_opy_ (u"ࠧࠨႺ"))
                        return
                    if r.hub_url:
                        f.bstack1llllll11l1_opy_(instance, driver, r.hub_url)
                        f.bstack1111111ll1_opy_(instance, bstack1llll1l1l1l_opy_.bstack1llllll1111_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1ll1l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧႻ"), e)
    def bstack1llllllll11_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll11l11_opy_.session_id(driver)
            if session_id:
                bstack111111l1l1_opy_ = bstack1ll1l_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤႼ").format(session_id)
                bstack1llll1l1l11_opy_.mark(bstack111111l1l1_opy_)
    def bstack1lllll1llll_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll1l1l1l_opy_.bstack1llll1ll111_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll11l11_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧႽ") + str(hub_url) + bstack1ll1l_opy_ (u"ࠤࠥႾ"))
            return
        framework_session_id = bstack1lllll11l11_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨႿ") + str(framework_session_id) + bstack1ll1l_opy_ (u"ࠦࠧჀ"))
            return
        if bstack1lllll11l11_opy_.bstack1111111l1l_opy_(*args) == bstack1lllll11l11_opy_.bstack1llllll1l1l_opy_:
            bstack1lllll1l1ll_opy_ = bstack1ll1l_opy_ (u"ࠧࢁࡽ࠻ࡧࡱࡨࠧჁ").format(framework_session_id)
            bstack111111l1l1_opy_ = bstack1ll1l_opy_ (u"ࠨࡻࡾ࠼ࡶࡸࡦࡸࡴࠣჂ").format(framework_session_id)
            bstack1llll1l1l11_opy_.end(
                label=bstack1ll1l_opy_ (u"ࠢࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾ࡵࡵࡳࡵ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠥჃ"),
                start=bstack111111l1l1_opy_,
                end=bstack1lllll1l1ll_opy_,
                status=True,
                failure=None
            )
            bstack1l11l11lll_opy_ = datetime.now()
            r = self.bstack111111l111_opy_(
                ref,
                f.get_state(instance, bstack1lllll11l11_opy_.bstack1lllllllll1_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺࠢჄ"), datetime.now() - bstack1l11l11lll_opy_)
            f.bstack1111111ll1_opy_(instance, bstack1llll1l1l1l_opy_.bstack1llll1ll111_opy_, r.success)
    def bstack1llll1lllll_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll1l1l1l_opy_.bstack1lllll111ll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll11l11_opy_.session_id(driver)
        hub_url = bstack1lllll11l11_opy_.hub_url(driver)
        bstack1l11l11lll_opy_ = datetime.now()
        r = self.bstack1lllll111l1_opy_(
            ref,
            f.get_state(instance, bstack1lllll11l11_opy_.bstack1lllllllll1_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶࠢჅ"), datetime.now() - bstack1l11l11lll_opy_)
        f.bstack1111111ll1_opy_(instance, bstack1llll1l1l1l_opy_.bstack1lllll111ll_opy_, r.success)
    @measure(event_name=EVENTS.bstack11l1111ll_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1lllll1l1l1_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣ჆") + str(req) + bstack1ll1l_opy_ (u"ࠦࠧჇ"))
        try:
            r = self.bstack1llll1l1ll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣ჈") + str(r.success) + bstack1ll1l_opy_ (u"ࠨࠢ჉"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ჊") + str(e) + bstack1ll1l_opy_ (u"ࠣࠤ჋"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack111111ll11_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1lllll1ll1l_opy_(
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
        self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦ჌") + str(req) + bstack1ll1l_opy_ (u"ࠥࠦჍ"))
        try:
            r = self.bstack1llll1l1ll1_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢ჎") + str(r.success) + bstack1ll1l_opy_ (u"ࠧࠨ჏"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦა") + str(e) + bstack1ll1l_opy_ (u"ࠢࠣბ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1ll1l1_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack111111l111_opy_(
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
        self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵ࠼ࠣࠦგ") + str(req) + bstack1ll1l_opy_ (u"ࠤࠥდ"))
        try:
            r = self.bstack1llll1l1ll1_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧე") + str(r) + bstack1ll1l_opy_ (u"ࠦࠧვ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥზ") + str(e) + bstack1ll1l_opy_ (u"ࠨࠢთ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllllll11l_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1lllll111l1_opy_(
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
        self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶ࠺ࠡࠤი") + str(req) + bstack1ll1l_opy_ (u"ࠣࠤკ"))
        try:
            r = self.bstack1llll1l1ll1_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦლ") + str(r) + bstack1ll1l_opy_ (u"ࠥࠦმ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤნ") + str(e) + bstack1ll1l_opy_ (u"ࠧࠨო"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack111l1l11l_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1llllll11ll_opy_(self, instance: bstack1llllllll1l_opy_, url: str, f: bstack1lllll11l11_opy_, kwargs):
        bstack1llllll1lll_opy_ = version.parse(f.framework_version)
        bstack111111l11l_opy_ = kwargs.get(bstack1ll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢპ"))
        bstack1lllllll1ll_opy_ = kwargs.get(bstack1ll1l_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢჟ"))
        bstack11111111l1_opy_ = {}
        bstack1111111l11_opy_ = {}
        bstack111111l1ll_opy_ = None
        bstack1llll1l1lll_opy_ = {}
        if bstack1lllllll1ll_opy_ is not None or bstack111111l11l_opy_ is not None: # check top level caps
            if bstack1lllllll1ll_opy_ is not None:
                bstack1llll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨრ")] = bstack1lllllll1ll_opy_
            if bstack111111l11l_opy_ is not None and callable(getattr(bstack111111l11l_opy_, bstack1ll1l_opy_ (u"ࠤࡷࡳࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦს"))):
                bstack1llll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࡣࡦࡹ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ტ")] = bstack111111l11l_opy_.to_capabilities()
        response = self.bstack1lllll1l1l1_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1llll1l1lll_opy_).encode(bstack1ll1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥუ")))
        if response is not None and response.capabilities:
            bstack11111111l1_opy_ = json.loads(response.capabilities.decode(bstack1ll1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦფ")))
            if not bstack11111111l1_opy_: # empty caps bstack1llllllllll_opy_ bstack1llll1llll1_opy_ bstack1llll1ll1ll_opy_ bstack11111111ll_opy_ or error in processing
                return
            bstack111111l1ll_opy_ = f.bstack1llll1l11ll_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥქ")](bstack11111111l1_opy_)
        if bstack111111l11l_opy_ is not None and bstack1llllll1lll_opy_ >= version.parse(bstack1ll1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ღ")):
            bstack1111111l11_opy_ = None
        if (
                not bstack111111l11l_opy_ and not bstack1lllllll1ll_opy_
        ) or (
                bstack1llllll1lll_opy_ < version.parse(bstack1ll1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧყ"))
        ):
            bstack1111111l11_opy_ = {}
            bstack1111111l11_opy_.update(bstack11111111l1_opy_)
        self.logger.info(bstack1l1l111l11_opy_)
        if os.environ.get(bstack1ll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠧშ")).lower().__eq__(bstack1ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣჩ")):
            kwargs.update(
                {
                    bstack1ll1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢც"): f.bstack1lllllll1l1_opy_,
                }
            )
        if bstack1llllll1lll_opy_ >= version.parse(bstack1ll1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬძ")):
            if bstack1lllllll1ll_opy_ is not None:
                del kwargs[bstack1ll1l_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨწ")]
            kwargs.update(
                {
                    bstack1ll1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣჭ"): bstack111111l1ll_opy_,
                    bstack1ll1l_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧხ"): True,
                    bstack1ll1l_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤჯ"): None,
                }
            )
        elif bstack1llllll1lll_opy_ >= version.parse(bstack1ll1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩჰ")):
            kwargs.update(
                {
                    bstack1ll1l_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦჱ"): bstack1111111l11_opy_,
                    bstack1ll1l_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨჲ"): bstack111111l1ll_opy_,
                    bstack1ll1l_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥჳ"): True,
                    bstack1ll1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢჴ"): None,
                }
            )
        elif bstack1llllll1lll_opy_ >= version.parse(bstack1ll1l_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨჵ")):
            kwargs.update(
                {
                    bstack1ll1l_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤჶ"): bstack1111111l11_opy_,
                    bstack1ll1l_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢჷ"): True,
                    bstack1ll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦჸ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1ll1l_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧჹ"): bstack1111111l11_opy_,
                    bstack1ll1l_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥჺ"): True,
                    bstack1ll1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢ჻"): None,
                }
            )