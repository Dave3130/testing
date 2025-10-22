# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll1l1_opy_ import (
    bstack1llll1lll1l_opy_,
    bstack1lllll1l1ll_opy_,
    bstack1lllllll1l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll11l1l_opy_ import bstack1lllll11111_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack11l1l11l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1l11l1l11_opy_ import bstack1llllll11ll_opy_
class bstack1llll11l11l_opy_(bstack1lllll11lll_opy_):
    bstack1lllll11l11_opy_ = bstack111l1l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸࠧ჈")
    bstack1llllll1l1l_opy_ = bstack111l1l_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺࠢ჉")
    bstack1llll1l11ll_opy_ = bstack111l1l_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶࠢ჊")
    def __init__(self, bstack1lllll1l11l_opy_):
        super().__init__()
        bstack1lllll11111_opy_.bstack1lllllll111_opy_((bstack1llll1lll1l_opy_.bstack1llllllllll_opy_, bstack1lllll1l1ll_opy_.PRE), self.bstack1llll1ll11l_opy_)
        bstack1lllll11111_opy_.bstack1lllllll111_opy_((bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_, bstack1lllll1l1ll_opy_.PRE), self.bstack1lllll1lll1_opy_)
        bstack1lllll11111_opy_.bstack1lllllll111_opy_((bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_, bstack1lllll1l1ll_opy_.POST), self.bstack1lllllll1ll_opy_)
        bstack1lllll11111_opy_.bstack1lllllll111_opy_((bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_, bstack1lllll1l1ll_opy_.POST), self.bstack111111111l_opy_)
        bstack1lllll11111_opy_.bstack1lllllll111_opy_((bstack1llll1lll1l_opy_.QUIT, bstack1lllll1l1ll_opy_.POST), self.bstack1lllll1l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1ll11l_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack111l1l_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥ჋"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack111l1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧ჌")), str):
                    url = kwargs.get(bstack111l1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨჍ"))
                elif hasattr(kwargs.get(bstack111l1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢ჎")), bstack111l1l_opy_ (u"ࠬࡥࡣ࡭࡫ࡨࡲࡹࡥࡣࡰࡰࡩ࡭࡬࠭჏")):
                    url = kwargs.get(bstack111l1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤა"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack111l1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥბ"))._url
            except Exception as e:
                url = bstack111l1l_opy_ (u"ࠨࠩგ")
                self.logger.error(bstack111l1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡷࡵࡰࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀࢃࠢდ").format(e))
            self.logger.info(bstack111l1l_opy_ (u"ࠥࡖࡪࡳ࡯ࡵࡧࠣࡗࡪࡸࡶࡦࡴࠣࡅࡩࡪࡲࡦࡵࡶࠤࡧ࡫ࡩ࡯ࡩࠣࡴࡦࡹࡳࡦࡦࠣࡥࡸࠦ࠺ࠡࡽࢀࠦე").format(str(url)))
            self.bstack1lllll11ll1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack111l1l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࡽ࠻ࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤვ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1lllll1lll1_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llll11l11l_opy_.bstack1lllll11l11_opy_, False):
            return
        if not f.bstack1llll1l1l11_opy_(instance, bstack1lllll11111_opy_.bstack1llll11llll_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll11111_opy_.bstack1llll11llll_opy_)
        if f.bstack1llll11l1ll_opy_(method_name, *args) and len(args) > 1:
            bstack1l1ll111ll_opy_ = datetime.now()
            hub_url = bstack1lllll11111_opy_.hub_url(driver)
            self.logger.warning(bstack111l1l_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࡃࠢზ") + str(hub_url) + bstack111l1l_opy_ (u"ࠨࠢთ"))
            bstack1llllll1111_opy_ = args[1][bstack111l1l_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨი")] if isinstance(args[1], dict) and bstack111l1l_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢკ") in args[1] else None
            bstack1lllll1ll1l_opy_ = bstack111l1l_opy_ (u"ࠤࡤࡰࡼࡧࡹࡴࡏࡤࡸࡨ࡮ࠢლ")
            if isinstance(bstack1llllll1111_opy_, dict):
                bstack1l1ll111ll_opy_ = datetime.now()
                r = self.bstack1llll1l1111_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴࠣმ"), datetime.now() - bstack1l1ll111ll_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack111l1l_opy_ (u"ࠦࡸࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪ࠾ࠥࠨნ") + str(r) + bstack111l1l_opy_ (u"ࠧࠨო"))
                        return
                    if r.hub_url:
                        f.bstack1llll11l111_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1l111l_opy_(instance, bstack1llll11l11l_opy_.bstack1lllll11l11_opy_, True)
                except Exception as e:
                    self.logger.error(bstack111l1l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧპ"), e)
    def bstack1lllllll1ll_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll11111_opy_.session_id(driver)
            if session_id:
                bstack1llll11l1l1_opy_ = bstack111l1l_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤჟ").format(session_id)
                bstack1llllll11ll_opy_.mark(bstack1llll11l1l1_opy_)
    def bstack111111111l_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11l11l_opy_.bstack1llllll1l1l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll11111_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack111l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧრ") + str(hub_url) + bstack111l1l_opy_ (u"ࠤࠥს"))
            return
        framework_session_id = bstack1lllll11111_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack111l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨტ") + str(framework_session_id) + bstack111l1l_opy_ (u"ࠦࠧუ"))
            return
        if bstack1lllll11111_opy_.bstack1lllllll11l_opy_(*args) == bstack1lllll11111_opy_.bstack1llll1llll1_opy_:
            bstack1llllllll11_opy_ = bstack111l1l_opy_ (u"ࠧࢁࡽ࠻ࡧࡱࡨࠧფ").format(framework_session_id)
            bstack1llll11l1l1_opy_ = bstack111l1l_opy_ (u"ࠨࡻࡾ࠼ࡶࡸࡦࡸࡴࠣქ").format(framework_session_id)
            bstack1llllll11ll_opy_.end(
                label=bstack111l1l_opy_ (u"ࠢࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾ࡵࡵࡳࡵ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠥღ"),
                start=bstack1llll11l1l1_opy_,
                end=bstack1llllllll11_opy_,
                status=True,
                failure=None
            )
            bstack1l1ll111ll_opy_ = datetime.now()
            r = self.bstack1lllllllll1_opy_(
                ref,
                f.get_state(instance, bstack1lllll11111_opy_.bstack1llll11llll_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺࠢყ"), datetime.now() - bstack1l1ll111ll_opy_)
            f.bstack1llll1l111l_opy_(instance, bstack1llll11l11l_opy_.bstack1llllll1l1l_opy_, r.success)
    def bstack1lllll1l111_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11l11l_opy_.bstack1llll1l11ll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll11111_opy_.session_id(driver)
        hub_url = bstack1lllll11111_opy_.hub_url(driver)
        bstack1l1ll111ll_opy_ = datetime.now()
        r = self.bstack1111111111_opy_(
            ref,
            f.get_state(instance, bstack1lllll11111_opy_.bstack1llll11llll_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶࠢშ"), datetime.now() - bstack1l1ll111ll_opy_)
        f.bstack1llll1l111l_opy_(instance, bstack1llll11l11l_opy_.bstack1llll1l11ll_opy_, r.success)
    @measure(event_name=EVENTS.bstack11l111ll11_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack1llllll111l_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack111l1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣჩ") + str(req) + bstack111l1l_opy_ (u"ࠦࠧც"))
        try:
            r = self.bstack1llll11ll11_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack111l1l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣძ") + str(r.success) + bstack111l1l_opy_ (u"ࠨࠢწ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧჭ") + str(e) + bstack111l1l_opy_ (u"ࠣࠤხ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1lllll_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack1llll1l1111_opy_(
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
        self.logger.debug(bstack111l1l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦჯ") + str(req) + bstack111l1l_opy_ (u"ࠥࠦჰ"))
        try:
            r = self.bstack1llll11ll11_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack111l1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢჱ") + str(r.success) + bstack111l1l_opy_ (u"ࠧࠨჲ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦჳ") + str(e) + bstack111l1l_opy_ (u"ࠢࠣჴ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1l1ll1_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack1lllllllll1_opy_(
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
        self.logger.debug(bstack111l1l_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵ࠼ࠣࠦჵ") + str(req) + bstack111l1l_opy_ (u"ࠤࠥჶ"))
        try:
            r = self.bstack1llll11ll11_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack111l1l_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧჷ") + str(r) + bstack111l1l_opy_ (u"ࠦࠧჸ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥჹ") + str(e) + bstack111l1l_opy_ (u"ࠨࠢჺ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll111l1_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack1111111111_opy_(
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
        self.logger.debug(bstack111l1l_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶ࠺ࠡࠤ჻") + str(req) + bstack111l1l_opy_ (u"ࠣࠤჼ"))
        try:
            r = self.bstack1llll11ll11_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack111l1l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦჽ") + str(r) + bstack111l1l_opy_ (u"ࠥࠦჾ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤჿ") + str(e) + bstack111l1l_opy_ (u"ࠧࠨᄀ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lll11111l_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack1lllll11ll1_opy_(self, instance: bstack1lllllll1l1_opy_, url: str, f: bstack1lllll11111_opy_, kwargs):
        bstack1llll1l1lll_opy_ = version.parse(f.framework_version)
        bstack1llll1ll1ll_opy_ = kwargs.get(bstack111l1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᄁ"))
        bstack1llll1ll111_opy_ = kwargs.get(bstack111l1l_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄂ"))
        bstack1lllll1l1l1_opy_ = {}
        bstack1llllll1ll1_opy_ = {}
        bstack1llll1l1l1l_opy_ = None
        bstack1lllll1llll_opy_ = {}
        if bstack1llll1ll111_opy_ is not None or bstack1llll1ll1ll_opy_ is not None: # check top level caps
            if bstack1llll1ll111_opy_ is not None:
                bstack1lllll1llll_opy_[bstack111l1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᄃ")] = bstack1llll1ll111_opy_
            if bstack1llll1ll1ll_opy_ is not None and callable(getattr(bstack1llll1ll1ll_opy_, bstack111l1l_opy_ (u"ࠤࡷࡳࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄄ"))):
                bstack1lllll1llll_opy_[bstack111l1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࡣࡦࡹ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᄅ")] = bstack1llll1ll1ll_opy_.to_capabilities()
        response = self.bstack1llllll111l_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll1llll_opy_).encode(bstack111l1l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᄆ")))
        if response is not None and response.capabilities:
            bstack1lllll1l1l1_opy_ = json.loads(response.capabilities.decode(bstack111l1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᄇ")))
            if not bstack1lllll1l1l1_opy_: # empty caps bstack1lllll111ll_opy_ bstack1lllll1111l_opy_ bstack1llllll1l11_opy_ bstack1lllll1ll11_opy_ or error in processing
                return
            bstack1llll1l1l1l_opy_ = f.bstack1llll11lll1_opy_[bstack111l1l_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥᄈ")](bstack1lllll1l1l1_opy_)
        if bstack1llll1ll1ll_opy_ is not None and bstack1llll1l1lll_opy_ >= version.parse(bstack111l1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᄉ")):
            bstack1llllll1ll1_opy_ = None
        if (
                not bstack1llll1ll1ll_opy_ and not bstack1llll1ll111_opy_
        ) or (
                bstack1llll1l1lll_opy_ < version.parse(bstack111l1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᄊ"))
        ):
            bstack1llllll1ll1_opy_ = {}
            bstack1llllll1ll1_opy_.update(bstack1lllll1l1l1_opy_)
        self.logger.info(bstack11l1l11l1l_opy_)
        if os.environ.get(bstack111l1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠧᄋ")).lower().__eq__(bstack111l1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᄌ")):
            kwargs.update(
                {
                    bstack111l1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᄍ"): f.bstack1llll11ll1l_opy_,
                }
            )
        if bstack1llll1l1lll_opy_ >= version.parse(bstack111l1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬᄎ")):
            if bstack1llll1ll111_opy_ is not None:
                del kwargs[bstack111l1l_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄏ")]
            kwargs.update(
                {
                    bstack111l1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᄐ"): bstack1llll1l1l1l_opy_,
                    bstack111l1l_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧᄑ"): True,
                    bstack111l1l_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤᄒ"): None,
                }
            )
        elif bstack1llll1l1lll_opy_ >= version.parse(bstack111l1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᄓ")):
            kwargs.update(
                {
                    bstack111l1l_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄔ"): bstack1llllll1ll1_opy_,
                    bstack111l1l_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᄕ"): bstack1llll1l1l1l_opy_,
                    bstack111l1l_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᄖ"): True,
                    bstack111l1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᄗ"): None,
                }
            )
        elif bstack1llll1l1lll_opy_ >= version.parse(bstack111l1l_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨᄘ")):
            kwargs.update(
                {
                    bstack111l1l_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄙ"): bstack1llllll1ll1_opy_,
                    bstack111l1l_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢᄚ"): True,
                    bstack111l1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦᄛ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack111l1l_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄜ"): bstack1llllll1ll1_opy_,
                    bstack111l1l_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᄝ"): True,
                    bstack111l1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᄞ"): None,
                }
            )