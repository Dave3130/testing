# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import (
    bstack1llll1l1lll_opy_,
    bstack1111111l1l_opy_,
    bstack1111111111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1llllll11l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack11l1111111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1l1l1111ll_opy_ import bstack111111111l_opy_
class bstack1lllllll11l_opy_(bstack1lllll1l111_opy_):
    bstack111111ll11_opy_ = bstack11l1l11_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶࠥႣ")
    bstack111111l1ll_opy_ = bstack11l1l11_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸࠧႤ")
    bstack1lllll11l11_opy_ = bstack11l1l11_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴࠧႥ")
    def __init__(self, bstack1lllll11lll_opy_):
        super().__init__()
        bstack1llllll11l1_opy_.bstack111111l11l_opy_((bstack1llll1l1lll_opy_.bstack1111111lll_opy_, bstack1111111l1l_opy_.PRE), self.bstack1lllll1l11l_opy_)
        bstack1llllll11l1_opy_.bstack111111l11l_opy_((bstack1llll1l1lll_opy_.bstack1llllll1111_opy_, bstack1111111l1l_opy_.PRE), self.bstack1lllll1l1l1_opy_)
        bstack1llllll11l1_opy_.bstack111111l11l_opy_((bstack1llll1l1lll_opy_.bstack1llllll1111_opy_, bstack1111111l1l_opy_.POST), self.bstack1lllll1lll1_opy_)
        bstack1llllll11l1_opy_.bstack111111l11l_opy_((bstack1llll1l1lll_opy_.bstack1llllll1111_opy_, bstack1111111l1l_opy_.POST), self.bstack1lllllllll1_opy_)
        bstack1llllll11l1_opy_.bstack111111l11l_opy_((bstack1llll1l1lll_opy_.QUIT, bstack1111111l1l_opy_.POST), self.bstack1lllllll1l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1l11l_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l1l11_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣႦ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11l1l11_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥႧ")), str):
                    url = kwargs.get(bstack11l1l11_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦႨ"))
                elif hasattr(kwargs.get(bstack11l1l11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧႩ")), bstack11l1l11_opy_ (u"ࠪࡣࡨࡲࡩࡦࡰࡷࡣࡨࡵ࡮ࡧ࡫ࡪࠫႪ")):
                    url = kwargs.get(bstack11l1l11_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢႫ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣႬ"))._url
            except Exception as e:
                url = bstack11l1l11_opy_ (u"࠭ࠧႭ")
                self.logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡵࡳ࡮ࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࢁࠧႮ").format(e))
            self.logger.info(bstack11l1l11_opy_ (u"ࠣࡔࡨࡱࡴࡺࡥࠡࡕࡨࡶࡻ࡫ࡲࠡࡃࡧࡨࡷ࡫ࡳࡴࠢࡥࡩ࡮ࡴࡧࠡࡲࡤࡷࡸ࡫ࡤࠡࡣࡶࠤ࠿ࠦࡻࡾࠤႯ").format(str(url)))
            self.bstack1llll1ll1ll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11l1l11_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࡿࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࢂࡀࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢႰ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1lllll1l1l1_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1lllllll11l_opy_.bstack111111ll11_opy_, False):
            return
        if not f.bstack1111111ll1_opy_(instance, bstack1llllll11l1_opy_.bstack1llll1ll111_opy_):
            return
        platform_index = f.get_state(instance, bstack1llllll11l1_opy_.bstack1llll1ll111_opy_)
        if f.bstack1llll1lll1l_opy_(method_name, *args) and len(args) > 1:
            bstack1l11lll1l_opy_ = datetime.now()
            hub_url = bstack1llllll11l1_opy_.hub_url(driver)
            self.logger.warning(bstack11l1l11_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧႱ") + str(hub_url) + bstack11l1l11_opy_ (u"ࠦࠧႲ"))
            bstack1llll1l1ll1_opy_ = args[1][bstack11l1l11_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦႳ")] if isinstance(args[1], dict) and bstack11l1l11_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧႴ") in args[1] else None
            bstack1lllll111ll_opy_ = bstack11l1l11_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧႵ")
            if isinstance(bstack1llll1l1ll1_opy_, dict):
                bstack1l11lll1l_opy_ = datetime.now()
                r = self.bstack1llll1lllll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࠨႶ"), datetime.now() - bstack1l11lll1l_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11l1l11_opy_ (u"ࠤࡶࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨ࠼ࠣࠦႷ") + str(r) + bstack11l1l11_opy_ (u"ࠥࠦႸ"))
                        return
                    if r.hub_url:
                        f.bstack1lllll1llll_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1l1l1l_opy_(instance, bstack1lllllll11l_opy_.bstack111111ll11_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11l1l11_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥႹ"), e)
    def bstack1lllll1lll1_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llllll11l1_opy_.session_id(driver)
            if session_id:
                bstack1llllll1ll1_opy_ = bstack11l1l11_opy_ (u"ࠧࢁࡽ࠻ࡵࡷࡥࡷࡺࠢႺ").format(session_id)
                bstack111111111l_opy_.mark(bstack1llllll1ll1_opy_)
    def bstack1lllllllll1_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllllll11l_opy_.bstack111111l1ll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llllll11l1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥႻ") + str(hub_url) + bstack11l1l11_opy_ (u"ࠢࠣႼ"))
            return
        framework_session_id = bstack1llllll11l1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦႽ") + str(framework_session_id) + bstack11l1l11_opy_ (u"ࠤࠥႾ"))
            return
        if bstack1llllll11l1_opy_.bstack1llll1lll11_opy_(*args) == bstack1llllll11l1_opy_.bstack1llll1l1l11_opy_:
            bstack1lllllll1ll_opy_ = bstack11l1l11_opy_ (u"ࠥࡿࢂࡀࡥ࡯ࡦࠥႿ").format(framework_session_id)
            bstack1llllll1ll1_opy_ = bstack11l1l11_opy_ (u"ࠦࢀࢃ࠺ࡴࡶࡤࡶࡹࠨჀ").format(framework_session_id)
            bstack111111111l_opy_.end(
                label=bstack11l1l11_opy_ (u"ࠧࡹࡤ࡬࠼ࡧࡶ࡮ࡼࡥࡳ࠼ࡳࡳࡸࡺ࠭ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠣჁ"),
                start=bstack1llllll1ll1_opy_,
                end=bstack1lllllll1ll_opy_,
                status=True,
                failure=None
            )
            bstack1l11lll1l_opy_ = datetime.now()
            r = self.bstack1llllllllll_opy_(
                ref,
                f.get_state(instance, bstack1llllll11l1_opy_.bstack1llll1ll111_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸࠧჂ"), datetime.now() - bstack1l11lll1l_opy_)
            f.bstack1llll1l1l1l_opy_(instance, bstack1lllllll11l_opy_.bstack111111l1ll_opy_, r.success)
    def bstack1lllllll1l1_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllllll11l_opy_.bstack1lllll11l11_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llllll11l1_opy_.session_id(driver)
        hub_url = bstack1llllll11l1_opy_.hub_url(driver)
        bstack1l11lll1l_opy_ = datetime.now()
        r = self.bstack1llllll1lll_opy_(
            ref,
            f.get_state(instance, bstack1llllll11l1_opy_.bstack1llll1ll111_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴࠧჃ"), datetime.now() - bstack1l11lll1l_opy_)
        f.bstack1llll1l1l1l_opy_(instance, bstack1lllllll11l_opy_.bstack1lllll11l11_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1ll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack111111l111_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨჄ") + str(req) + bstack11l1l11_opy_ (u"ࠤࠥჅ"))
        try:
            r = self.bstack1llll1ll11l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨ჆") + str(r.success) + bstack11l1l11_opy_ (u"ࠦࠧჇ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥ჈") + str(e) + bstack11l1l11_opy_ (u"ࠨࠢ჉"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll111l1_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1llll1lllll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llllllll11_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤ჊") + str(req) + bstack11l1l11_opy_ (u"ࠣࠤ჋"))
        try:
            r = self.bstack1llll1ll11l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࡷࡺࡩࡣࡦࡵࡶࡁࠧ჌") + str(r.success) + bstack11l1l11_opy_ (u"ࠥࠦჍ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤ჎") + str(e) + bstack11l1l11_opy_ (u"ࠧࠨ჏"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll1l11_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1llllllllll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllllll11_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11l1l11_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺ࠺ࠡࠤა") + str(req) + bstack11l1l11_opy_ (u"ࠢࠣბ"))
        try:
            r = self.bstack1llll1ll11l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥგ") + str(r) + bstack11l1l11_opy_ (u"ࠤࠥდ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣე") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧვ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11111_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1llllll1lll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllllll11_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11l1l11_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴ࠿ࠦࠢზ") + str(req) + bstack11l1l11_opy_ (u"ࠨࠢთ"))
        try:
            r = self.bstack1llll1ll11l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤი") + str(r) + bstack11l1l11_opy_ (u"ࠣࠤკ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢლ") + str(e) + bstack11l1l11_opy_ (u"ࠥࠦმ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1lllll1_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1llll1ll1ll_opy_(self, instance: bstack1111111111_opy_, url: str, f: bstack1llllll11l1_opy_, kwargs):
        bstack1lllll1ll1l_opy_ = version.parse(f.framework_version)
        bstack1llllll1l1l_opy_ = kwargs.get(bstack11l1l11_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧნ"))
        bstack1lllll11ll1_opy_ = kwargs.get(bstack11l1l11_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧო"))
        bstack1111111l11_opy_ = {}
        bstack1llll1llll1_opy_ = {}
        bstack111111l1l1_opy_ = None
        bstack1lllll1l1ll_opy_ = {}
        if bstack1lllll11ll1_opy_ is not None or bstack1llllll1l1l_opy_ is not None: # check top level caps
            if bstack1lllll11ll1_opy_ is not None:
                bstack1lllll1l1ll_opy_[bstack11l1l11_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭პ")] = bstack1lllll11ll1_opy_
            if bstack1llllll1l1l_opy_ is not None and callable(getattr(bstack1llllll1l1l_opy_, bstack11l1l11_opy_ (u"ࠢࡵࡱࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤჟ"))):
                bstack1lllll1l1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡤࡷࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫრ")] = bstack1llllll1l1l_opy_.to_capabilities()
        response = self.bstack111111l111_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll1l1ll_opy_).encode(bstack11l1l11_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣს")))
        if response is not None and response.capabilities:
            bstack1111111l11_opy_ = json.loads(response.capabilities.decode(bstack11l1l11_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤტ")))
            if not bstack1111111l11_opy_: # empty caps bstack1lllll1ll11_opy_ bstack1lllll1111l_opy_ bstack11111111ll_opy_ bstack1llll1ll1l1_opy_ or error in processing
                return
            bstack111111l1l1_opy_ = f.bstack1llllll11ll_opy_[bstack11l1l11_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡣࡴࡶࡴࡪࡱࡱࡷࡤ࡬ࡲࡰ࡯ࡢࡧࡦࡶࡳࠣუ")](bstack1111111l11_opy_)
        if bstack1llllll1l1l_opy_ is not None and bstack1lllll1ll1l_opy_ >= version.parse(bstack11l1l11_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫფ")):
            bstack1llll1llll1_opy_ = None
        if (
                not bstack1llllll1l1l_opy_ and not bstack1lllll11ll1_opy_
        ) or (
                bstack1lllll1ll1l_opy_ < version.parse(bstack11l1l11_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬქ"))
        ):
            bstack1llll1llll1_opy_ = {}
            bstack1llll1llll1_opy_.update(bstack1111111l11_opy_)
        self.logger.info(bstack11l1111111_opy_)
        if os.environ.get(bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠥღ")).lower().__eq__(bstack11l1l11_opy_ (u"ࠣࡶࡵࡹࡪࠨყ")):
            kwargs.update(
                {
                    bstack11l1l11_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧშ"): f.bstack1llllllll1l_opy_,
                }
            )
        if bstack1lllll1ll1l_opy_ >= version.parse(bstack11l1l11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪჩ")):
            if bstack1lllll11ll1_opy_ is not None:
                del kwargs[bstack11l1l11_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦც")]
            kwargs.update(
                {
                    bstack11l1l11_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨძ"): bstack111111l1l1_opy_,
                    bstack11l1l11_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥწ"): True,
                    bstack11l1l11_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢჭ"): None,
                }
            )
        elif bstack1lllll1ll1l_opy_ >= version.parse(bstack11l1l11_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧხ")):
            kwargs.update(
                {
                    bstack11l1l11_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤჯ"): bstack1llll1llll1_opy_,
                    bstack11l1l11_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦჰ"): bstack111111l1l1_opy_,
                    bstack11l1l11_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣჱ"): True,
                    bstack11l1l11_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧჲ"): None,
                }
            )
        elif bstack1lllll1ll1l_opy_ >= version.parse(bstack11l1l11_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ჳ")):
            kwargs.update(
                {
                    bstack11l1l11_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢჴ"): bstack1llll1llll1_opy_,
                    bstack11l1l11_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧჵ"): True,
                    bstack11l1l11_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤჶ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11l1l11_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥჷ"): bstack1llll1llll1_opy_,
                    bstack11l1l11_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣჸ"): True,
                    bstack11l1l11_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧჹ"): None,
                }
            )