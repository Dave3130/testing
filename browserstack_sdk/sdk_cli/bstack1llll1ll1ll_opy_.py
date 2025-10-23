# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack11l1llll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
class bstack1lllll111l1_opy_(bstack1llllll111l_opy_):
    bstack1111111lll_opy_ = bstack111111l_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺࠢႠ")
    bstack1llll1l1l11_opy_ = bstack111111l_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵࠤႡ")
    bstack1lllll1ll1l_opy_ = bstack111111l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱࠤႢ")
    def __init__(self, bstack111111l11l_opy_):
        super().__init__()
        bstack1llllll11ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack111111l111_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1lllll1ll11_opy_)
        bstack1llllll11ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.PRE), self.bstack111111l1l1_opy_)
        bstack1llllll11ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.POST), self.bstack1llllll1ll1_opy_)
        bstack1llllll11ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.POST), self.bstack1llllll1111_opy_)
        bstack1llllll11ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.QUIT, bstack1llll1ll111_opy_.POST), self.bstack1llllll1l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1ll11_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111111l_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧႣ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack111111l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢႤ")), str):
                    url = kwargs.get(bstack111111l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣႥ"))
                elif hasattr(kwargs.get(bstack111111l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤႦ")), bstack111111l_opy_ (u"ࠧࡠࡥ࡯࡭ࡪࡴࡴࡠࡥࡲࡲ࡫࡯ࡧࠨႧ")):
                    url = kwargs.get(bstack111111l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦႨ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack111111l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧႩ"))._url
            except Exception as e:
                url = bstack111111l_opy_ (u"ࠪࠫႪ")
                self.logger.error(bstack111111l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡹࡷࡲࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠿ࠦࡻࡾࠤႫ").format(e))
            self.logger.info(bstack111111l_opy_ (u"ࠧࡘࡥ࡮ࡱࡷࡩ࡙ࠥࡥࡳࡸࡨࡶࠥࡇࡤࡥࡴࡨࡷࡸࠦࡢࡦ࡫ࡱ࡫ࠥࡶࡡࡴࡵࡨࡨࠥࡧࡳࠡ࠼ࠣࡿࢂࠨႬ").format(str(url)))
            self.bstack1llll1ll1l1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack111111l_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷ࠴ࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࡼࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࡿ࠽ࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦႭ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack111111l1l1_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1lllll111l1_opy_.bstack1111111lll_opy_, False):
            return
        if not f.bstack1lllllll11l_opy_(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_):
            return
        platform_index = f.get_state(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_)
        if f.bstack1llllllllll_opy_(method_name, *args) and len(args) > 1:
            bstack1111ll111_opy_ = datetime.now()
            hub_url = bstack1llllll11ll_opy_.hub_url(driver)
            self.logger.warning(bstack111111l_opy_ (u"ࠢࡩࡷࡥࡣࡺࡸ࡬࠾ࠤႮ") + str(hub_url) + bstack111111l_opy_ (u"ࠣࠤႯ"))
            bstack1lllllll1ll_opy_ = args[1][bstack111111l_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣႰ")] if isinstance(args[1], dict) and bstack111111l_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤႱ") in args[1] else None
            bstack1lllll1llll_opy_ = bstack111111l_opy_ (u"ࠦࡦࡲࡷࡢࡻࡶࡑࡦࡺࡣࡩࠤႲ")
            if isinstance(bstack1lllllll1ll_opy_, dict):
                bstack1111ll111_opy_ = datetime.now()
                r = self.bstack1lllllll1l1_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶࠥႳ"), datetime.now() - bstack1111ll111_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack111111l_opy_ (u"ࠨࡳࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࡀࠠࠣႴ") + str(r) + bstack111111l_opy_ (u"ࠢࠣႵ"))
                        return
                    if r.hub_url:
                        f.bstack1lllll1l11l_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1lll1l_opy_(instance, bstack1lllll111l1_opy_.bstack1111111lll_opy_, True)
                except Exception as e:
                    self.logger.error(bstack111111l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႶ"), e)
    def bstack1llllll1ll1_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llllll11ll_opy_.session_id(driver)
            if session_id:
                bstack111111l1ll_opy_ = bstack111111l_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦႷ").format(session_id)
                bstack1llllll1lll_opy_.mark(bstack111111l1ll_opy_)
    def bstack1llllll1111_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll111l1_opy_.bstack1llll1l1l11_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llllll11ll_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack111111l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥ࡮ࡵࡣࡡࡸࡶࡱࡃࠢႸ") + str(hub_url) + bstack111111l_opy_ (u"ࠦࠧႹ"))
            return
        framework_session_id = bstack1llllll11ll_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack111111l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠽ࠣႺ") + str(framework_session_id) + bstack111111l_opy_ (u"ࠨࠢႻ"))
            return
        if bstack1llllll11ll_opy_.bstack1111111111_opy_(*args) == bstack1llllll11ll_opy_.bstack1llll1ll11l_opy_:
            bstack1111111l1l_opy_ = bstack111111l_opy_ (u"ࠢࡼࡿ࠽ࡩࡳࡪࠢႼ").format(framework_session_id)
            bstack111111l1ll_opy_ = bstack111111l_opy_ (u"ࠣࡽࢀ࠾ࡸࡺࡡࡳࡶࠥႽ").format(framework_session_id)
            bstack1llllll1lll_opy_.end(
                label=bstack111111l_opy_ (u"ࠤࡶࡨࡰࡀࡤࡳ࡫ࡹࡩࡷࡀࡰࡰࡵࡷ࠱࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠧႾ"),
                start=bstack111111l1ll_opy_,
                end=bstack1111111l1l_opy_,
                status=True,
                failure=None
            )
            bstack1111ll111_opy_ = datetime.now()
            r = self.bstack1llllllll11_opy_(
                ref,
                f.get_state(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵࠤႿ"), datetime.now() - bstack1111ll111_opy_)
            f.bstack1llll1lll1l_opy_(instance, bstack1lllll111l1_opy_.bstack1llll1l1l11_opy_, r.success)
    def bstack1llllll1l11_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll111l1_opy_.bstack1lllll1ll1l_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llllll11ll_opy_.session_id(driver)
        hub_url = bstack1llllll11ll_opy_.hub_url(driver)
        bstack1111ll111_opy_ = datetime.now()
        r = self.bstack1llll1l11ll_opy_(
            ref,
            f.get_state(instance, bstack1llllll11ll_opy_.bstack1llllllll1l_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱࠤჀ"), datetime.now() - bstack1111ll111_opy_)
        f.bstack1llll1lll1l_opy_(instance, bstack1lllll111l1_opy_.bstack1lllll1ll1l_opy_, r.success)
    @measure(event_name=EVENTS.bstack11ll1l1ll1_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1lllll1lll1_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack111111l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥჁ") + str(req) + bstack111111l_opy_ (u"ࠨࠢჂ"))
        try:
            r = self.bstack111111111l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack111111l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥჃ") + str(r.success) + bstack111111l_opy_ (u"ࠣࠤჄ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢჅ") + str(e) + bstack111111l_opy_ (u"ࠥࠦ჆"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack111111ll11_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1lllllll1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llll1l1ll1_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack111111l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨჇ") + str(req) + bstack111111l_opy_ (u"ࠧࠨ჈"))
        try:
            r = self.bstack111111111l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack111111l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤ჉") + str(r.success) + bstack111111l_opy_ (u"ࠢࠣ჊"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ჋") + str(e) + bstack111111l_opy_ (u"ࠤࠥ჌"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1111111ll1_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1llllllll11_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1l1ll1_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack111111l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡢࡴࡷ࠾ࠥࠨჍ") + str(req) + bstack111111l_opy_ (u"ࠦࠧ჎"))
        try:
            r = self.bstack111111111l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack111111l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢ჏") + str(r) + bstack111111l_opy_ (u"ࠨࠢა"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧბ") + str(e) + bstack111111l_opy_ (u"ࠣࠤგ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll111ll_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1llll1l11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1l1ll1_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack111111l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱ࠼ࠣࠦდ") + str(req) + bstack111111l_opy_ (u"ࠥࠦე"))
        try:
            r = self.bstack111111111l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack111111l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨვ") + str(r) + bstack111111l_opy_ (u"ࠧࠨზ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦთ") + str(e) + bstack111111l_opy_ (u"ࠢࠣი"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1111l1l11l_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1llll1ll1l1_opy_(self, instance: bstack1lllll11l1l_opy_, url: str, f: bstack1llllll11ll_opy_, kwargs):
        bstack11111111ll_opy_ = version.parse(f.framework_version)
        bstack1lllll1l111_opy_ = kwargs.get(bstack111111l_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤკ"))
        bstack1lllll1l1l1_opy_ = kwargs.get(bstack111111l_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤლ"))
        bstack1lllll11lll_opy_ = {}
        bstack1llllll1l1l_opy_ = {}
        bstack1lllllll111_opy_ = None
        bstack1lllll11ll1_opy_ = {}
        if bstack1lllll1l1l1_opy_ is not None or bstack1lllll1l111_opy_ is not None: # check top level caps
            if bstack1lllll1l1l1_opy_ is not None:
                bstack1lllll11ll1_opy_[bstack111111l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪმ")] = bstack1lllll1l1l1_opy_
            if bstack1lllll1l111_opy_ is not None and callable(getattr(bstack1lllll1l111_opy_, bstack111111l_opy_ (u"ࠦࡹࡵ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨნ"))):
                bstack1lllll11ll1_opy_[bstack111111l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸࡥࡡࡴࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨო")] = bstack1lllll1l111_opy_.to_capabilities()
        response = self.bstack1lllll1lll1_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll11ll1_opy_).encode(bstack111111l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧპ")))
        if response is not None and response.capabilities:
            bstack1lllll11lll_opy_ = json.loads(response.capabilities.decode(bstack111111l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨჟ")))
            if not bstack1lllll11lll_opy_: # empty caps bstack1llll1llll1_opy_ bstack1lllll11111_opy_ bstack1lllll11l11_opy_ bstack1llll1l1l1l_opy_ or error in processing
                return
            bstack1lllllll111_opy_ = f.bstack1llll1l1lll_opy_[bstack111111l_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡩࡶࡴࡳ࡟ࡤࡣࡳࡷࠧრ")](bstack1lllll11lll_opy_)
        if bstack1lllll1l111_opy_ is not None and bstack11111111ll_opy_ >= version.parse(bstack111111l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨს")):
            bstack1llllll1l1l_opy_ = None
        if (
                not bstack1lllll1l111_opy_ and not bstack1lllll1l1l1_opy_
        ) or (
                bstack11111111ll_opy_ < version.parse(bstack111111l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩტ"))
        ):
            bstack1llllll1l1l_opy_ = {}
            bstack1llllll1l1l_opy_.update(bstack1lllll11lll_opy_)
        self.logger.info(bstack11l1llll1l_opy_)
        if os.environ.get(bstack111111l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠢუ")).lower().__eq__(bstack111111l_opy_ (u"ࠧࡺࡲࡶࡧࠥფ")):
            kwargs.update(
                {
                    bstack111111l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤქ"): f.bstack1lllll1111l_opy_,
                }
            )
        if bstack11111111ll_opy_ >= version.parse(bstack111111l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧღ")):
            if bstack1lllll1l1l1_opy_ is not None:
                del kwargs[bstack111111l_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣყ")]
            kwargs.update(
                {
                    bstack111111l_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥშ"): bstack1lllllll111_opy_,
                    bstack111111l_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢჩ"): True,
                    bstack111111l_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦც"): None,
                }
            )
        elif bstack11111111ll_opy_ >= version.parse(bstack111111l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫძ")):
            kwargs.update(
                {
                    bstack111111l_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨწ"): bstack1llllll1l1l_opy_,
                    bstack111111l_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣჭ"): bstack1lllllll111_opy_,
                    bstack111111l_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧხ"): True,
                    bstack111111l_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤჯ"): None,
                }
            )
        elif bstack11111111ll_opy_ >= version.parse(bstack111111l_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪჰ")):
            kwargs.update(
                {
                    bstack111111l_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦჱ"): bstack1llllll1l1l_opy_,
                    bstack111111l_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤჲ"): True,
                    bstack111111l_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨჳ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack111111l_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢჴ"): bstack1llllll1l1l_opy_,
                    bstack111111l_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧჵ"): True,
                    bstack111111l_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤჶ"): None,
                }
            )