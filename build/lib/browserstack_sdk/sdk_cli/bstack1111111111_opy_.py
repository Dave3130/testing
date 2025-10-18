# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll1lll1ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
class bstack1llll11l111_opy_(bstack1lllllllll1_opy_):
    bstack1lllll1llll_opy_ = bstack11ll_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸࠧ჏")
    bstack1lllll11lll_opy_ = bstack11ll_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺࠢა")
    bstack1llll1l1lll_opy_ = bstack11ll_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶࠢბ")
    def __init__(self, bstack1llll11lll1_opy_):
        super().__init__()
        bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1llll1_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1llll1l1111_opy_)
        bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1llll1lll1l_opy_)
        bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.POST), self.bstack1llll11llll_opy_)
        bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.POST), self.bstack1lllll1111l_opy_)
        bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.QUIT, bstack1lllll1ll1l_opy_.POST), self.bstack1llll1l11ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1l1111_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥგ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧდ")), str):
                    url = kwargs.get(bstack11ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨე"))
                elif hasattr(kwargs.get(bstack11ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢვ")), bstack11ll_opy_ (u"ࠬࡥࡣ࡭࡫ࡨࡲࡹࡥࡣࡰࡰࡩ࡭࡬࠭ზ")):
                    url = kwargs.get(bstack11ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤთ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥი"))._url
            except Exception as e:
                url = bstack11ll_opy_ (u"ࠨࠩკ")
                self.logger.error(bstack11ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡷࡵࡰࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀࢃࠢლ").format(e))
            self.logger.info(bstack11ll_opy_ (u"ࠥࡖࡪࡳ࡯ࡵࡧࠣࡗࡪࡸࡶࡦࡴࠣࡅࡩࡪࡲࡦࡵࡶࠤࡧ࡫ࡩ࡯ࡩࠣࡴࡦࡹࡳࡦࡦࠣࡥࡸࠦ࠺ࠡࡽࢀࠦმ").format(str(url)))
            self.bstack1lllll1lll1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11ll_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࡂࢁࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࡽ࠻ࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤნ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1llll1lll1l_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llll11l111_opy_.bstack1lllll1llll_opy_, False):
            return
        if not f.bstack1lllllll111_opy_(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_)
        if f.bstack1lllll11ll1_opy_(method_name, *args) and len(args) > 1:
            bstack1l11111lll_opy_ = datetime.now()
            hub_url = bstack1lllll1l1l1_opy_.hub_url(driver)
            self.logger.warning(bstack11ll_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࡃࠢო") + str(hub_url) + bstack11ll_opy_ (u"ࠨࠢპ"))
            bstack1llll1ll111_opy_ = args[1][bstack11ll_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨჟ")] if isinstance(args[1], dict) and bstack11ll_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢრ") in args[1] else None
            bstack1llll11l1ll_opy_ = bstack11ll_opy_ (u"ࠤࡤࡰࡼࡧࡹࡴࡏࡤࡸࡨ࡮ࠢს")
            if isinstance(bstack1llll1ll111_opy_, dict):
                bstack1l11111lll_opy_ = datetime.now()
                r = self.bstack1llll1l11l1_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴࠣტ"), datetime.now() - bstack1l11111lll_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11ll_opy_ (u"ࠦࡸࡵ࡭ࡦࡶ࡫࡭ࡳ࡭ࠠࡸࡧࡱࡸࠥࡽࡲࡰࡰࡪ࠾ࠥࠨუ") + str(r) + bstack11ll_opy_ (u"ࠧࠨფ"))
                        return
                    if r.hub_url:
                        f.bstack1llllll111l_opy_(instance, driver, r.hub_url)
                        f.bstack1llllll1lll_opy_(instance, bstack1llll11l111_opy_.bstack1lllll1llll_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11ll_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧქ"), e)
    def bstack1llll11llll_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll1l1l1_opy_.session_id(driver)
            if session_id:
                bstack1llll11l1l1_opy_ = bstack11ll_opy_ (u"ࠢࡼࡿ࠽ࡷࡹࡧࡲࡵࠤღ").format(session_id)
                bstack1llll11ll11_opy_.mark(bstack1llll11l1l1_opy_)
    def bstack1lllll1111l_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11l111_opy_.bstack1lllll11lll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll1l1l1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧყ") + str(hub_url) + bstack11ll_opy_ (u"ࠤࠥშ"))
            return
        framework_session_id = bstack1lllll1l1l1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨჩ") + str(framework_session_id) + bstack11ll_opy_ (u"ࠦࠧც"))
            return
        if bstack1lllll1l1l1_opy_.bstack1llll1l1l1l_opy_(*args) == bstack1lllll1l1l1_opy_.bstack1llll1ll11l_opy_:
            bstack1llll1ll1ll_opy_ = bstack11ll_opy_ (u"ࠧࢁࡽ࠻ࡧࡱࡨࠧძ").format(framework_session_id)
            bstack1llll11l1l1_opy_ = bstack11ll_opy_ (u"ࠨࡻࡾ࠼ࡶࡸࡦࡸࡴࠣწ").format(framework_session_id)
            bstack1llll11ll11_opy_.end(
                label=bstack11ll_opy_ (u"ࠢࡴࡦ࡮࠾ࡩࡸࡩࡷࡧࡵ࠾ࡵࡵࡳࡵ࠯࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡦࡺࡩࡰࡰࠥჭ"),
                start=bstack1llll11l1l1_opy_,
                end=bstack1llll1ll1ll_opy_,
                status=True,
                failure=None
            )
            bstack1l11111lll_opy_ = datetime.now()
            r = self.bstack1llllll11ll_opy_(
                ref,
                f.get_state(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺࠢხ"), datetime.now() - bstack1l11111lll_opy_)
            f.bstack1llllll1lll_opy_(instance, bstack1llll11l111_opy_.bstack1lllll11lll_opy_, r.success)
    def bstack1llll1l11ll_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11l111_opy_.bstack1llll1l1lll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll1l1l1_opy_.session_id(driver)
        hub_url = bstack1lllll1l1l1_opy_.hub_url(driver)
        bstack1l11111lll_opy_ = datetime.now()
        r = self.bstack1llllllll1l_opy_(
            ref,
            f.get_state(instance, bstack1lllll1l1l1_opy_.bstack1llll1l111l_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶࠢჯ"), datetime.now() - bstack1l11111lll_opy_)
        f.bstack1llllll1lll_opy_(instance, bstack1llll11l111_opy_.bstack1llll1l1lll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1111l11l1l_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1llll1lll11_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11ll_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣჰ") + str(req) + bstack11ll_opy_ (u"ࠦࠧჱ"))
        try:
            r = self.bstack1lllll11111_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࡳࡶࡥࡦࡩࡸࡹ࠽ࠣჲ") + str(r.success) + bstack11ll_opy_ (u"ࠨࠢჳ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧჴ") + str(e) + bstack11ll_opy_ (u"ࠣࠤჵ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll1l11_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1llll1l11l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1lllll111ll_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11ll_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦჶ") + str(req) + bstack11ll_opy_ (u"ࠥࠦჷ"))
        try:
            r = self.bstack1lllll11111_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11ll_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢჸ") + str(r.success) + bstack11ll_opy_ (u"ࠧࠨჹ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦჺ") + str(e) + bstack11ll_opy_ (u"ࠢࠣ჻"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllllllll_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1llllll11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1lllll111ll_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11ll_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵ࠼ࠣࠦჼ") + str(req) + bstack11ll_opy_ (u"ࠤࠥჽ"))
        try:
            r = self.bstack1lllll11111_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11ll_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧჾ") + str(r) + bstack11ll_opy_ (u"ࠦࠧჿ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥᄀ") + str(e) + bstack11ll_opy_ (u"ࠨࠢᄁ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1l1l11_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1llllllll1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1lllll111ll_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11ll_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡴࡶ࠺ࠡࠤᄂ") + str(req) + bstack11ll_opy_ (u"ࠣࠤᄃ"))
        try:
            r = self.bstack1lllll11111_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11ll_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᄄ") + str(r) + bstack11ll_opy_ (u"ࠥࠦᄅ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᄆ") + str(e) + bstack11ll_opy_ (u"ࠧࠨᄇ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll1l1lll1_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1lllll1lll1_opy_(self, instance: bstack1lllll11l1l_opy_, url: str, f: bstack1lllll1l1l1_opy_, kwargs):
        bstack111111111l_opy_ = version.parse(f.framework_version)
        bstack1llllll1111_opy_ = kwargs.get(bstack11ll_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᄈ"))
        bstack1lllllll1ll_opy_ = kwargs.get(bstack11ll_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄉ"))
        bstack1llllll11l1_opy_ = {}
        bstack1llll1l1ll1_opy_ = {}
        bstack1llll11ll1l_opy_ = None
        bstack1lllll1ll11_opy_ = {}
        if bstack1lllllll1ll_opy_ is not None or bstack1llllll1111_opy_ is not None: # check top level caps
            if bstack1lllllll1ll_opy_ is not None:
                bstack1lllll1ll11_opy_[bstack11ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᄊ")] = bstack1lllllll1ll_opy_
            if bstack1llllll1111_opy_ is not None and callable(getattr(bstack1llllll1111_opy_, bstack11ll_opy_ (u"ࠤࡷࡳࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄋ"))):
                bstack1lllll1ll11_opy_[bstack11ll_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࡣࡦࡹ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᄌ")] = bstack1llllll1111_opy_.to_capabilities()
        response = self.bstack1llll1lll11_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll1ll11_opy_).encode(bstack11ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᄍ")))
        if response is not None and response.capabilities:
            bstack1llllll11l1_opy_ = json.loads(response.capabilities.decode(bstack11ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᄎ")))
            if not bstack1llllll11l1_opy_: # empty caps bstack1llllllll11_opy_ bstack1lllll1l111_opy_ bstack1lllll11l11_opy_ bstack1llll11l11l_opy_ or error in processing
                return
            bstack1llll11ll1l_opy_ = f.bstack1lllllll1l1_opy_[bstack11ll_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥᄏ")](bstack1llllll11l1_opy_)
        if bstack1llllll1111_opy_ is not None and bstack111111111l_opy_ >= version.parse(bstack11ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᄐ")):
            bstack1llll1l1ll1_opy_ = None
        if (
                not bstack1llllll1111_opy_ and not bstack1lllllll1ll_opy_
        ) or (
                bstack111111111l_opy_ < version.parse(bstack11ll_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᄑ"))
        ):
            bstack1llll1l1ll1_opy_ = {}
            bstack1llll1l1ll1_opy_.update(bstack1llllll11l1_opy_)
        self.logger.info(bstack1ll1lll1ll_opy_)
        if os.environ.get(bstack11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠧᄒ")).lower().__eq__(bstack11ll_opy_ (u"ࠥࡸࡷࡻࡥࠣᄓ")):
            kwargs.update(
                {
                    bstack11ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᄔ"): f.bstack1lllll111l1_opy_,
                }
            )
        if bstack111111111l_opy_ >= version.parse(bstack11ll_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬᄕ")):
            if bstack1lllllll1ll_opy_ is not None:
                del kwargs[bstack11ll_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄖ")]
            kwargs.update(
                {
                    bstack11ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᄗ"): bstack1llll11ll1l_opy_,
                    bstack11ll_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧᄘ"): True,
                    bstack11ll_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤᄙ"): None,
                }
            )
        elif bstack111111111l_opy_ >= version.parse(bstack11ll_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᄚ")):
            kwargs.update(
                {
                    bstack11ll_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄛ"): bstack1llll1l1ll1_opy_,
                    bstack11ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᄜ"): bstack1llll11ll1l_opy_,
                    bstack11ll_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᄝ"): True,
                    bstack11ll_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᄞ"): None,
                }
            )
        elif bstack111111111l_opy_ >= version.parse(bstack11ll_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨᄟ")):
            kwargs.update(
                {
                    bstack11ll_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄠ"): bstack1llll1l1ll1_opy_,
                    bstack11ll_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢᄡ"): True,
                    bstack11ll_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦᄢ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11ll_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄣ"): bstack1llll1l1ll1_opy_,
                    bstack11ll_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᄤ"): True,
                    bstack11ll_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᄥ"): None,
                }
            )