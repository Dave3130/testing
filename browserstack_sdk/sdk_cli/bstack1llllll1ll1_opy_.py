# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import (
    bstack1llll11llll_opy_,
    bstack1llll11l1l1_opy_,
    bstack1llll1l1l11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import bstack1llll11ll11_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack111l1ll1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
class bstack1llll1l111l_opy_(bstack1lllll1l111_opy_):
    bstack1llllll1l11_opy_ = bstack11ll1l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣ࡮ࡴࡩࡵࠤლ")
    bstack1lllll1l11l_opy_ = bstack11ll1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡢࡴࡷࠦმ")
    bstack1lllll1l1ll_opy_ = bstack11ll1l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡱࡳࠦნ")
    def __init__(self, bstack1lllll1l1l1_opy_):
        super().__init__()
        bstack1llll11ll11_opy_.bstack1lllll111ll_opy_((bstack1llll11llll_opy_.bstack1llll11ll1l_opy_, bstack1llll11l1l1_opy_.PRE), self.bstack1llllll11ll_opy_)
        bstack1llll11ll11_opy_.bstack1lllll111ll_opy_((bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_, bstack1llll11l1l1_opy_.PRE), self.bstack1lllll1111l_opy_)
        bstack1llll11ll11_opy_.bstack1lllll111ll_opy_((bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_, bstack1llll11l1l1_opy_.POST), self.bstack1llllll111l_opy_)
        bstack1llll11ll11_opy_.bstack1lllll111ll_opy_((bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_, bstack1llll11l1l1_opy_.POST), self.bstack1lllll1ll1l_opy_)
        bstack1llll11ll11_opy_.bstack1lllll111ll_opy_((bstack1llll11llll_opy_.QUIT, bstack1llll11l1l1_opy_.POST), self.bstack1llll1lll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllll11ll_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll1l_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢო"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤპ")), str):
                    url = kwargs.get(bstack11ll1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥჟ"))
                elif hasattr(kwargs.get(bstack11ll1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦრ")), bstack11ll1l_opy_ (u"ࠩࡢࡧࡱ࡯ࡥ࡯ࡶࡢࡧࡴࡴࡦࡪࡩࠪს")):
                    url = kwargs.get(bstack11ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨტ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11ll1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢუ"))._url
            except Exception as e:
                url = bstack11ll1l_opy_ (u"ࠬ࠭ფ")
                self.logger.error(bstack11ll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡻࡲ࡭ࠢࡩࡶࡴࡳࠠࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽࢀࠦქ").format(e))
            self.logger.info(bstack11ll1l_opy_ (u"ࠢࡓࡧࡰࡳࡹ࡫ࠠࡔࡧࡵࡺࡪࡸࠠࡂࡦࡧࡶࡪࡹࡳࠡࡤࡨ࡭ࡳ࡭ࠠࡱࡣࡶࡷࡪࡪࠠࡢࡵࠣ࠾ࠥࢁࡽࠣღ").format(str(url)))
            self.bstack1llll1lllll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11ll1l_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹ࠿ࡾࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࢁ࠿ࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨყ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1lllll1111l_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llll1l111l_opy_.bstack1llllll1l11_opy_, False):
            return
        if not f.bstack1llllllll11_opy_(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_):
            return
        platform_index = f.get_state(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_)
        if f.bstack1lllll1ll11_opy_(method_name, *args) and len(args) > 1:
            bstack1ll11ll111_opy_ = datetime.now()
            hub_url = bstack1llll11ll11_opy_.hub_url(driver)
            self.logger.warning(bstack11ll1l_opy_ (u"ࠤ࡫ࡹࡧࡥࡵࡳ࡮ࡀࠦშ") + str(hub_url) + bstack11ll1l_opy_ (u"ࠥࠦჩ"))
            bstack1llllll1111_opy_ = args[1][bstack11ll1l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥც")] if isinstance(args[1], dict) and bstack11ll1l_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦძ") in args[1] else None
            bstack1lllll11lll_opy_ = bstack11ll1l_opy_ (u"ࠨࡡ࡭ࡹࡤࡽࡸࡓࡡࡵࡥ࡫ࠦწ")
            if isinstance(bstack1llllll1111_opy_, dict):
                bstack1ll11ll111_opy_ = datetime.now()
                r = self.bstack1lllll11l1l_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸࠧჭ"), datetime.now() - bstack1ll11ll111_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11ll1l_opy_ (u"ࠣࡵࡲࡱࡪࡺࡨࡪࡰࡪࠤࡼ࡫࡮ࡵࠢࡺࡶࡴࡴࡧ࠻ࠢࠥხ") + str(r) + bstack11ll1l_opy_ (u"ࠤࠥჯ"))
                        return
                    if r.hub_url:
                        f.bstack1llllll1lll_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1l1lll_opy_(instance, bstack1llll1l111l_opy_.bstack1llllll1l11_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11ll1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤჰ"), e)
    def bstack1llllll111l_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llll11ll11_opy_.session_id(driver)
            if session_id:
                bstack1lllll11l11_opy_ = bstack11ll1l_opy_ (u"ࠦࢀࢃ࠺ࡴࡶࡤࡶࡹࠨჱ").format(session_id)
                bstack1llll111ll1_opy_.mark(bstack1lllll11l11_opy_)
    def bstack1lllll1ll1l_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll1l111l_opy_.bstack1lllll1l11l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llll11ll11_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡩࡷࡥࡣࡺࡸ࡬࠾ࠤჲ") + str(hub_url) + bstack11ll1l_opy_ (u"ࠨࠢჳ"))
            return
        framework_session_id = bstack1llll11ll11_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11ll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠿ࠥჴ") + str(framework_session_id) + bstack11ll1l_opy_ (u"ࠣࠤჵ"))
            return
        if bstack1llll11ll11_opy_.bstack1llllll1l1l_opy_(*args) == bstack1llll11ll11_opy_.bstack1llll11l11l_opy_:
            bstack1llll111l1l_opy_ = bstack11ll1l_opy_ (u"ࠤࡾࢁ࠿࡫࡮ࡥࠤჶ").format(framework_session_id)
            bstack1lllll11l11_opy_ = bstack11ll1l_opy_ (u"ࠥࡿࢂࡀࡳࡵࡣࡵࡸࠧჷ").format(framework_session_id)
            bstack1llll111ll1_opy_.end(
                label=bstack11ll1l_opy_ (u"ࠦࡸࡪ࡫࠻ࡦࡵ࡭ࡻ࡫ࡲ࠻ࡲࡲࡷࡹ࠳ࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡣࡷ࡭ࡴࡴࠢჸ"),
                start=bstack1lllll11l11_opy_,
                end=bstack1llll111l1l_opy_,
                status=True,
                failure=None
            )
            bstack1ll11ll111_opy_ = datetime.now()
            r = self.bstack1llll1llll1_opy_(
                ref,
                f.get_state(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡢࡴࡷࠦჹ"), datetime.now() - bstack1ll11ll111_opy_)
            f.bstack1llll1l1lll_opy_(instance, bstack1llll1l111l_opy_.bstack1lllll1l11l_opy_, r.success)
    def bstack1llll1lll1l_opy_(
        self,
        f: bstack1llll11ll11_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll1l111l_opy_.bstack1lllll1l1ll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llll11ll11_opy_.session_id(driver)
        hub_url = bstack1llll11ll11_opy_.hub_url(driver)
        bstack1ll11ll111_opy_ = datetime.now()
        r = self.bstack1lllllll1l1_opy_(
            ref,
            f.get_state(instance, bstack1llll11ll11_opy_.bstack1lllll1llll_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡱࡳࠦჺ"), datetime.now() - bstack1ll11ll111_opy_)
        f.bstack1llll1l1lll_opy_(instance, bstack1llll1l111l_opy_.bstack1lllll1l1ll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1l1l1ll_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def bstack1llll1ll111_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡺࡩࡧࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࠽ࠤࠧ჻") + str(req) + bstack11ll1l_opy_ (u"ࠣࠤჼ"))
        try:
            r = self.bstack1lllll111l1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࡷࡺࡩࡣࡦࡵࡶࡁࠧჽ") + str(r.success) + bstack11ll1l_opy_ (u"ࠥࠦჾ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤჿ") + str(e) + bstack11ll1l_opy_ (u"ࠧࠨᄀ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll11l111_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def bstack1lllll11l1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llll1l11l1_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࡀࠠࠣᄁ") + str(req) + bstack11ll1l_opy_ (u"ࠢࠣᄂ"))
        try:
            r = self.bstack1lllll111l1_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦᄃ") + str(r.success) + bstack11ll1l_opy_ (u"ࠤࠥᄄ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣᄅ") + str(e) + bstack11ll1l_opy_ (u"ࠦࠧᄆ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll111lll_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def bstack1llll1llll1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1l11l1_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11ll1l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࡀࠠࠣᄇ") + str(req) + bstack11ll1l_opy_ (u"ࠨࠢᄈ"))
        try:
            r = self.bstack1lllll111l1_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᄉ") + str(r) + bstack11ll1l_opy_ (u"ࠣࠤᄊ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᄋ") + str(e) + bstack11ll1l_opy_ (u"ࠥࠦᄌ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1ll11l_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def bstack1lllllll1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1l11l1_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡱࡳ࠾ࠥࠨᄍ") + str(req) + bstack11ll1l_opy_ (u"ࠧࠨᄎ"))
        try:
            r = self.bstack1lllll111l1_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᄏ") + str(r) + bstack11ll1l_opy_ (u"ࠢࠣᄐ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᄑ") + str(e) + bstack11ll1l_opy_ (u"ࠤࠥᄒ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11llllll1_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def bstack1llll1lllll_opy_(self, instance: bstack1llll1l1l11_opy_, url: str, f: bstack1llll11ll11_opy_, kwargs):
        bstack1llll1l1ll1_opy_ = version.parse(f.framework_version)
        bstack1lllllll1ll_opy_ = kwargs.get(bstack11ll1l_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦᄓ"))
        bstack1lllllll11l_opy_ = kwargs.get(bstack11ll1l_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄔ"))
        bstack1llll11l1ll_opy_ = {}
        bstack1llll11lll1_opy_ = {}
        bstack1llll1ll1ll_opy_ = None
        bstack1lllllll111_opy_ = {}
        if bstack1lllllll11l_opy_ is not None or bstack1lllllll1ll_opy_ is not None: # check top level caps
            if bstack1lllllll11l_opy_ is not None:
                bstack1lllllll111_opy_[bstack11ll1l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᄕ")] = bstack1lllllll11l_opy_
            if bstack1lllllll1ll_opy_ is not None and callable(getattr(bstack1lllllll1ll_opy_, bstack11ll1l_opy_ (u"ࠨࡴࡰࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄖ"))):
                bstack1lllllll111_opy_[bstack11ll1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࡠࡣࡶࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᄗ")] = bstack1lllllll1ll_opy_.to_capabilities()
        response = self.bstack1llll1ll111_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllllll111_opy_).encode(bstack11ll1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᄘ")))
        if response is not None and response.capabilities:
            bstack1llll11l1ll_opy_ = json.loads(response.capabilities.decode(bstack11ll1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᄙ")))
            if not bstack1llll11l1ll_opy_: # empty caps bstack1llllllll1l_opy_ bstack1lllll1lll1_opy_ bstack1llll1l1111_opy_ bstack1llll1l1l1l_opy_ or error in processing
                return
            bstack1llll1ll1ll_opy_ = f.bstack1lllll11111_opy_[bstack11ll1l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡢࡳࡵࡺࡩࡰࡰࡶࡣ࡫ࡸ࡯࡮ࡡࡦࡥࡵࡹࠢᄚ")](bstack1llll11l1ll_opy_)
        if bstack1lllllll1ll_opy_ is not None and bstack1llll1l1ll1_opy_ >= version.parse(bstack11ll1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪᄛ")):
            bstack1llll11lll1_opy_ = None
        if (
                not bstack1lllllll1ll_opy_ and not bstack1lllllll11l_opy_
        ) or (
                bstack1llll1l1ll1_opy_ < version.parse(bstack11ll1l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᄜ"))
        ):
            bstack1llll11lll1_opy_ = {}
            bstack1llll11lll1_opy_.update(bstack1llll11l1ll_opy_)
        self.logger.info(bstack111l1ll1l1_opy_)
        if os.environ.get(bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠤᄝ")).lower().__eq__(bstack11ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧᄞ")):
            kwargs.update(
                {
                    bstack11ll1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᄟ"): f.bstack1llll1l11ll_opy_,
                }
            )
        if bstack1llll1l1ll1_opy_ >= version.parse(bstack11ll1l_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩᄠ")):
            if bstack1lllllll11l_opy_ is not None:
                del kwargs[bstack11ll1l_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᄡ")]
            kwargs.update(
                {
                    bstack11ll1l_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᄢ"): bstack1llll1ll1ll_opy_,
                    bstack11ll1l_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤᄣ"): True,
                    bstack11ll1l_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨᄤ"): None,
                }
            )
        elif bstack1llll1l1ll1_opy_ >= version.parse(bstack11ll1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᄥ")):
            kwargs.update(
                {
                    bstack11ll1l_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄦ"): bstack1llll11lll1_opy_,
                    bstack11ll1l_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᄧ"): bstack1llll1ll1ll_opy_,
                    bstack11ll1l_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢᄨ"): True,
                    bstack11ll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦᄩ"): None,
                }
            )
        elif bstack1llll1l1ll1_opy_ >= version.parse(bstack11ll1l_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬᄪ")):
            kwargs.update(
                {
                    bstack11ll1l_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄫ"): bstack1llll11lll1_opy_,
                    bstack11ll1l_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᄬ"): True,
                    bstack11ll1l_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᄭ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11ll1l_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄮ"): bstack1llll11lll1_opy_,
                    bstack11ll1l_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢᄯ"): True,
                    bstack11ll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦᄰ"): None,
                }
            )