# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
    bstack1111111l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll11l11l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
class bstack1lllll1l111_opy_(bstack1llll1ll11l_opy_):
    bstack1lllllll11l_opy_ = bstack1lllll1_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦႫ")
    bstack1lllll11lll_opy_ = bstack1lllll1_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࠨႬ")
    bstack1llll1l1l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࠨႭ")
    def __init__(self, bstack1llllll1l1l_opy_):
        super().__init__()
        bstack1lllll1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1llll1ll111_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack1llllll1lll_opy_)
        bstack1lllll1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack111111l1ll_opy_)
        bstack1lllll1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.POST), self.bstack111111l11l_opy_)
        bstack1lllll1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.POST), self.bstack1llllllll11_opy_)
        bstack1lllll1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.QUIT, bstack1lllll1lll1_opy_.POST), self.bstack111111l1l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllll1lll_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1_opy_ (u"ࠢࡠࡡ࡬ࡲ࡮ࡺ࡟ࡠࠤႮ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1lllll1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦႯ")), str):
                    url = kwargs.get(bstack1lllll1_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧႰ"))
                elif hasattr(kwargs.get(bstack1lllll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨႱ")), bstack1lllll1_opy_ (u"ࠫࡤࡩ࡬ࡪࡧࡱࡸࡤࡩ࡯࡯ࡨ࡬࡫ࠬႲ")):
                    url = kwargs.get(bstack1lllll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣႳ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1lllll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤႴ"))._url
            except Exception as e:
                url = bstack1lllll1_opy_ (u"ࠧࠨႵ")
                self.logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡴ࡯ࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࢂࠨႶ").format(e))
            self.logger.info(bstack1lllll1_opy_ (u"ࠤࡕࡩࡲࡵࡴࡦࠢࡖࡩࡷࡼࡥࡳࠢࡄࡨࡩࡸࡥࡴࡵࠣࡦࡪ࡯࡮ࡨࠢࡳࡥࡸࡹࡥࡥࠢࡤࡷࠥࡀࠠࡼࡿࠥႷ").format(str(url)))
            self.bstack1lllll1llll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1lllll1_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࢀࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࢃ࠺ࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣႸ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack111111l1ll_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1lllll1l111_opy_.bstack1lllllll11l_opy_, False):
            return
        if not f.bstack1llll1ll1l1_opy_(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_)
        if f.bstack1llllll111l_opy_(method_name, *args) and len(args) > 1:
            bstack1l11llll11_opy_ = datetime.now()
            hub_url = bstack1lllll1ll11_opy_.hub_url(driver)
            self.logger.warning(bstack1lllll1_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࡂࠨႹ") + str(hub_url) + bstack1lllll1_opy_ (u"ࠧࠨႺ"))
            bstack111111l111_opy_ = args[1][bstack1lllll1_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧႻ")] if isinstance(args[1], dict) and bstack1lllll1_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨႼ") in args[1] else None
            bstack1lllll1ll1l_opy_ = bstack1lllll1_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨႽ")
            if isinstance(bstack111111l111_opy_, dict):
                bstack1l11llll11_opy_ = datetime.now()
                r = self.bstack1111111lll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺࠢႾ"), datetime.now() - bstack1l11llll11_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1lllll1_opy_ (u"ࠥࡷࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩ࠽ࠤࠧႿ") + str(r) + bstack1lllll1_opy_ (u"ࠦࠧჀ"))
                        return
                    if r.hub_url:
                        f.bstack111111ll1l_opy_(instance, driver, r.hub_url)
                        f.bstack1lllll1l11l_opy_(instance, bstack1lllll1l111_opy_.bstack1lllllll11l_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1lllll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦჁ"), e)
    def bstack111111l11l_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll1ll11_opy_.session_id(driver)
            if session_id:
                bstack1llll1lll11_opy_ = bstack1lllll1_opy_ (u"ࠨࡻࡾ࠼ࡶࡸࡦࡸࡴࠣჂ").format(session_id)
                bstack1lllllllll1_opy_.mark(bstack1llll1lll11_opy_)
    def bstack1llllllll11_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1l111_opy_.bstack1lllll11lll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll1ll11_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1lllll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢ࡫ࡹࡧࡥࡵࡳ࡮ࡀࠦჃ") + str(hub_url) + bstack1lllll1_opy_ (u"ࠣࠤჄ"))
            return
        framework_session_id = bstack1lllll1ll11_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1lllll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࡁࠧჅ") + str(framework_session_id) + bstack1lllll1_opy_ (u"ࠥࠦ჆"))
            return
        if bstack1lllll1ll11_opy_.bstack1llllllllll_opy_(*args) == bstack1lllll1ll11_opy_.bstack1lllll11l11_opy_:
            bstack1llll1l1ll1_opy_ = bstack1lllll1_opy_ (u"ࠦࢀࢃ࠺ࡦࡰࡧࠦჇ").format(framework_session_id)
            bstack1llll1lll11_opy_ = bstack1lllll1_opy_ (u"ࠧࢁࡽ࠻ࡵࡷࡥࡷࡺࠢ჈").format(framework_session_id)
            bstack1lllllllll1_opy_.end(
                label=bstack1lllll1_opy_ (u"ࠨࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡴࡴࡹࡴ࠮࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠤ჉"),
                start=bstack1llll1lll11_opy_,
                end=bstack1llll1l1ll1_opy_,
                status=True,
                failure=None
            )
            bstack1l11llll11_opy_ = datetime.now()
            r = self.bstack1lllll1111l_opy_(
                ref,
                f.get_state(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࠨ჊"), datetime.now() - bstack1l11llll11_opy_)
            f.bstack1lllll1l11l_opy_(instance, bstack1lllll1l111_opy_.bstack1lllll11lll_opy_, r.success)
    def bstack111111l1l1_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1l111_opy_.bstack1llll1l1l1l_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll1ll11_opy_.session_id(driver)
        hub_url = bstack1lllll1ll11_opy_.hub_url(driver)
        bstack1l11llll11_opy_ = datetime.now()
        r = self.bstack1llllll1l11_opy_(
            ref,
            f.get_state(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࠨ჋"), datetime.now() - bstack1l11llll11_opy_)
        f.bstack1lllll1l11l_opy_(instance, bstack1lllll1l111_opy_.bstack1llll1l1l1l_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1ll1lll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1llllllll1l_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢ჌") + str(req) + bstack1lllll1_opy_ (u"ࠥࠦჍ"))
        try:
            r = self.bstack1111111l1l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢ჎") + str(r.success) + bstack1lllll1_opy_ (u"ࠧࠨ჏"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦა") + str(e) + bstack1lllll1_opy_ (u"ࠢࠣბ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11l1l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1111111lll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llll1lllll_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥგ") + str(req) + bstack1lllll1_opy_ (u"ࠤࠥდ"))
        try:
            r = self.bstack1111111l1l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨე") + str(r.success) + bstack1lllll1_opy_ (u"ࠦࠧვ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥზ") + str(e) + bstack1lllll1_opy_ (u"ࠨࠢთ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll111l1_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1lllll1111l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1lllll_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴ࠻ࠢࠥი") + str(req) + bstack1lllll1_opy_ (u"ࠣࠤკ"))
        try:
            r = self.bstack1111111l1l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦლ") + str(r) + bstack1lllll1_opy_ (u"ࠥࠦმ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤნ") + str(e) + bstack1lllll1_opy_ (u"ࠧࠨო"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1lll1l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1llllll1l11_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1lllll_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࡀࠠࠣპ") + str(req) + bstack1lllll1_opy_ (u"ࠢࠣჟ"))
        try:
            r = self.bstack1111111l1l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥრ") + str(r) + bstack1lllll1_opy_ (u"ࠤࠥს"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣტ") + str(e) + bstack1lllll1_opy_ (u"ࠦࠧუ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11llllll_opy_, stage=STAGE.bstack11l1l111l1_opy_)
    def bstack1lllll1llll_opy_(self, instance: bstack1111111l11_opy_, url: str, f: bstack1lllll1ll11_opy_, kwargs):
        bstack1lllll1l1ll_opy_ = version.parse(f.framework_version)
        bstack111111ll11_opy_ = kwargs.get(bstack1lllll1_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨფ"))
        bstack11111111l1_opy_ = kwargs.get(bstack1lllll1_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨქ"))
        bstack111111lll1_opy_ = {}
        bstack1lllll11ll1_opy_ = {}
        bstack1llllll11l1_opy_ = None
        bstack1lllllll1ll_opy_ = {}
        if bstack11111111l1_opy_ is not None or bstack111111ll11_opy_ is not None: # check top level caps
            if bstack11111111l1_opy_ is not None:
                bstack1lllllll1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧღ")] = bstack11111111l1_opy_
            if bstack111111ll11_opy_ is not None and callable(getattr(bstack111111ll11_opy_, bstack1lllll1_opy_ (u"ࠣࡶࡲࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥყ"))):
                bstack1lllllll1ll_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࡢࡥࡸࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬშ")] = bstack111111ll11_opy_.to_capabilities()
        response = self.bstack1llllllll1l_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllllll1ll_opy_).encode(bstack1lllll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤჩ")))
        if response is not None and response.capabilities:
            bstack111111lll1_opy_ = json.loads(response.capabilities.decode(bstack1lllll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥც")))
            if not bstack111111lll1_opy_: # empty caps bstack1llllll1111_opy_ bstack1llllll11ll_opy_ bstack1lllll11111_opy_ bstack1lllllll111_opy_ or error in processing
                return
            bstack1llllll11l1_opy_ = f.bstack111111111l_opy_[bstack1lllll1_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡤࡵࡰࡵ࡫ࡲࡲࡸࡥࡦࡳࡱࡰࡣࡨࡧࡰࡴࠤძ")](bstack111111lll1_opy_)
        if bstack111111ll11_opy_ is not None and bstack1lllll1l1ll_opy_ >= version.parse(bstack1lllll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬწ")):
            bstack1lllll11ll1_opy_ = None
        if (
                not bstack111111ll11_opy_ and not bstack11111111l1_opy_
        ) or (
                bstack1lllll1l1ll_opy_ < version.parse(bstack1lllll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ჭ"))
        ):
            bstack1lllll11ll1_opy_ = {}
            bstack1lllll11ll1_opy_.update(bstack111111lll1_opy_)
        self.logger.info(bstack1ll11l11l_opy_)
        if os.environ.get(bstack1lllll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠦხ")).lower().__eq__(bstack1lllll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢჯ")):
            kwargs.update(
                {
                    bstack1lllll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨჰ"): f.bstack1llll1llll1_opy_,
                }
            )
        if bstack1lllll1l1ll_opy_ >= version.parse(bstack1lllll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫჱ")):
            if bstack11111111l1_opy_ is not None:
                del kwargs[bstack1lllll1_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧჲ")]
            kwargs.update(
                {
                    bstack1lllll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢჳ"): bstack1llllll11l1_opy_,
                    bstack1lllll1_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦჴ"): True,
                    bstack1lllll1_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣჵ"): None,
                }
            )
        elif bstack1lllll1l1ll_opy_ >= version.parse(bstack1lllll1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨჶ")):
            kwargs.update(
                {
                    bstack1lllll1_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥჷ"): bstack1lllll11ll1_opy_,
                    bstack1lllll1_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧჸ"): bstack1llllll11l1_opy_,
                    bstack1lllll1_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤჹ"): True,
                    bstack1lllll1_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨჺ"): None,
                }
            )
        elif bstack1lllll1l1ll_opy_ >= version.parse(bstack1lllll1_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧ჻")):
            kwargs.update(
                {
                    bstack1lllll1_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣჼ"): bstack1lllll11ll1_opy_,
                    bstack1lllll1_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨჽ"): True,
                    bstack1lllll1_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥჾ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1lllll1_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦჿ"): bstack1lllll11ll1_opy_,
                    bstack1lllll1_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤᄀ"): True,
                    bstack1lllll1_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨᄁ"): None,
                }
            )