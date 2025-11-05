# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll111l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll1l_opy_ import (
    bstack1llll1l1ll1_opy_,
    bstack1llll11llll_opy_,
    bstack1llll111l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1ll111_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1lll1l11ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
class bstack1llll11l1ll_opy_(bstack1lllll111l1_opy_):
    bstack1llll1ll11l_opy_ = bstack11ll1ll_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺࠢჟ")
    bstack1lllll1111l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵࠤრ")
    bstack1llll111lll_opy_ = bstack11ll1ll_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱࠤს")
    def __init__(self, bstack1lllll1lll1_opy_):
        super().__init__()
        bstack1llll1ll111_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llllllll1l_opy_, bstack1llll11llll_opy_.PRE), self.bstack1lllll1ll11_opy_)
        bstack1llll1ll111_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_, bstack1llll11llll_opy_.PRE), self.bstack1lllll1ll1l_opy_)
        bstack1llll1ll111_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_, bstack1llll11llll_opy_.POST), self.bstack1llllll1l11_opy_)
        bstack1llll1ll111_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.bstack1llll1lll11_opy_, bstack1llll11llll_opy_.POST), self.bstack1llllll1111_opy_)
        bstack1llll1ll111_opy_.bstack1lllll1l11l_opy_((bstack1llll1l1ll1_opy_.QUIT, bstack1llll11llll_opy_.POST), self.bstack1lllll11l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1ll11_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11ll1ll_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧტ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11ll1ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢუ")), str):
                    url = kwargs.get(bstack11ll1ll_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣფ"))
                elif hasattr(kwargs.get(bstack11ll1ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤქ")), bstack11ll1ll_opy_ (u"ࠧࡠࡥ࡯࡭ࡪࡴࡴࡠࡥࡲࡲ࡫࡯ࡧࠨღ")):
                    url = kwargs.get(bstack11ll1ll_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦყ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11ll1ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧშ"))._url
            except Exception as e:
                url = bstack11ll1ll_opy_ (u"ࠪࠫჩ")
                self.logger.error(bstack11ll1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡹࡷࡲࠠࡧࡴࡲࡱࠥࡪࡲࡪࡸࡨࡶ࠿ࠦࡻࡾࠤც").format(e))
            self.logger.info(bstack11ll1ll_opy_ (u"ࠧࡘࡥ࡮ࡱࡷࡩ࡙ࠥࡥࡳࡸࡨࡶࠥࡇࡤࡥࡴࡨࡷࡸࠦࡢࡦ࡫ࡱ࡫ࠥࡶࡡࡴࡵࡨࡨࠥࡧࡳࠡ࠼ࠣࡿࢂࠨძ").format(str(url)))
            self.bstack1lllll11111_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11ll1ll_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷ࠴ࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾ࠽ࡼࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࡿ࠽ࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࡾ࡯ࡼࡧࡲࡨࡵࢀࠦწ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1lllll1ll1l_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llll11l1ll_opy_.bstack1llll1ll11l_opy_, False):
            return
        if not f.bstack1lllll1llll_opy_(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_):
            return
        platform_index = f.get_state(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_)
        if f.bstack1llll1l1111_opy_(method_name, *args) and len(args) > 1:
            bstack111111ll11_opy_ = datetime.now()
            hub_url = bstack1llll1ll111_opy_.hub_url(driver)
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠢࡩࡷࡥࡣࡺࡸ࡬࠾ࠤჭ") + str(hub_url) + bstack11ll1ll_opy_ (u"ࠣࠤხ"))
            bstack1llll11lll1_opy_ = args[1][bstack11ll1ll_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣჯ")] if isinstance(args[1], dict) and bstack11ll1ll_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤჰ") in args[1] else None
            bstack1llllll11l1_opy_ = bstack11ll1ll_opy_ (u"ࠦࡦࡲࡷࡢࡻࡶࡑࡦࡺࡣࡩࠤჱ")
            if isinstance(bstack1llll11lll1_opy_, dict):
                bstack111111ll11_opy_ = datetime.now()
                r = self.bstack1lllllll1ll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶࠥჲ"), datetime.now() - bstack111111ll11_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11ll1ll_opy_ (u"ࠨࡳࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࡀࠠࠣჳ") + str(r) + bstack11ll1ll_opy_ (u"ࠢࠣჴ"))
                        return
                    if r.hub_url:
                        f.bstack1llll1lllll_opy_(instance, driver, r.hub_url)
                        f.bstack1lllllll1l1_opy_(instance, bstack1llll11l1ll_opy_.bstack1llll1ll11l_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢჵ"), e)
    def bstack1llllll1l11_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llll1ll111_opy_.session_id(driver)
            if session_id:
                bstack1llll1l111l_opy_ = bstack11ll1ll_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦჶ").format(session_id)
                bstack1llll11l11l_opy_.mark(bstack1llll1l111l_opy_)
    def bstack1llllll1111_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11l1ll_opy_.bstack1lllll1111l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llll1ll111_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥ࡮ࡵࡣࡡࡸࡶࡱࡃࠢჷ") + str(hub_url) + bstack11ll1ll_opy_ (u"ࠦࠧჸ"))
            return
        framework_session_id = bstack1llll1ll111_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11ll1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠽ࠣჹ") + str(framework_session_id) + bstack11ll1ll_opy_ (u"ࠨࠢჺ"))
            return
        if bstack1llll1ll111_opy_.bstack1llll1ll1l1_opy_(*args) == bstack1llll1ll111_opy_.bstack1lllllll11l_opy_:
            bstack1llll11l1l1_opy_ = bstack11ll1ll_opy_ (u"ࠢࡼࡿ࠽ࡩࡳࡪࠢ჻").format(framework_session_id)
            bstack1llll1l111l_opy_ = bstack11ll1ll_opy_ (u"ࠣࡽࢀ࠾ࡸࡺࡡࡳࡶࠥჼ").format(framework_session_id)
            bstack1llll11l11l_opy_.end(
                label=bstack11ll1ll_opy_ (u"ࠤࡶࡨࡰࡀࡤࡳ࡫ࡹࡩࡷࡀࡰࡰࡵࡷ࠱࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡡࡵ࡫ࡲࡲࠧჽ"),
                start=bstack1llll1l111l_opy_,
                end=bstack1llll11l1l1_opy_,
                status=True,
                failure=None
            )
            bstack111111ll11_opy_ = datetime.now()
            r = self.bstack1llll1llll1_opy_(
                ref,
                f.get_state(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡷࡹࡧࡲࡵࠤჾ"), datetime.now() - bstack111111ll11_opy_)
            f.bstack1lllllll1l1_opy_(instance, bstack1llll11l1ll_opy_.bstack1lllll1111l_opy_, r.success)
    def bstack1lllll11l1l_opy_(
        self,
        f: bstack1llll1ll111_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll1l1ll1_opy_, bstack1llll11llll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11l1ll_opy_.bstack1llll111lll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llll1ll111_opy_.session_id(driver)
        hub_url = bstack1llll1ll111_opy_.hub_url(driver)
        bstack111111ll11_opy_ = datetime.now()
        r = self.bstack1llll11ll1l_opy_(
            ref,
            f.get_state(instance, bstack1llll1ll111_opy_.bstack1llll1l11ll_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱࠤჿ"), datetime.now() - bstack111111ll11_opy_)
        f.bstack1lllllll1l1_opy_(instance, bstack1llll11l1ll_opy_.bstack1llll111lll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1l11lll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1lllll11lll_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥᄀ") + str(req) + bstack11ll1ll_opy_ (u"ࠨࠢᄁ"))
        try:
            r = self.bstack1llllll1l1l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥᄂ") + str(r.success) + bstack11ll1ll_opy_ (u"ࠣࠤᄃ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᄄ") + str(e) + bstack11ll1ll_opy_ (u"ࠥࠦᄅ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11l11_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1lllllll1ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llllll1ll1_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨᄆ") + str(req) + bstack11ll1ll_opy_ (u"ࠧࠨᄇ"))
        try:
            r = self.bstack1llllll1l1l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࡴࡷࡦࡧࡪࡹࡳ࠾ࠤᄈ") + str(r.success) + bstack11ll1ll_opy_ (u"ࠢࠣᄉ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᄊ") + str(e) + bstack11ll1ll_opy_ (u"ࠤࠥᄋ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1l1l1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1llll1llll1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllll1ll1_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡢࡴࡷ࠾ࠥࠨᄌ") + str(req) + bstack11ll1ll_opy_ (u"ࠦࠧᄍ"))
        try:
            r = self.bstack1llllll1l1l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᄎ") + str(r) + bstack11ll1ll_opy_ (u"ࠨࠢᄏ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᄐ") + str(e) + bstack11ll1ll_opy_ (u"ࠣࠤᄑ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1llll11ll1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllll1ll1_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺ࡯ࡱ࠼ࠣࠦᄒ") + str(req) + bstack11ll1ll_opy_ (u"ࠥࠦᄓ"))
        try:
            r = self.bstack1llllll1l1l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨᄔ") + str(r) + bstack11ll1ll_opy_ (u"ࠧࠨᄕ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦᄖ") + str(e) + bstack11ll1ll_opy_ (u"ࠢࠣᄗ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11l11ll11_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
    def bstack1lllll11111_opy_(self, instance: bstack1llll111l1l_opy_, url: str, f: bstack1llll1ll111_opy_, kwargs):
        bstack1llll1l1l11_opy_ = version.parse(f.framework_version)
        bstack1llll11l111_opy_ = kwargs.get(bstack11ll1ll_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᄘ"))
        bstack1llll1l1lll_opy_ = kwargs.get(bstack11ll1ll_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄙ"))
        bstack1llllllll11_opy_ = {}
        bstack1lllll1l1l1_opy_ = {}
        bstack1llll11ll11_opy_ = None
        bstack1lllll111ll_opy_ = {}
        if bstack1llll1l1lll_opy_ is not None or bstack1llll11l111_opy_ is not None: # check top level caps
            if bstack1llll1l1lll_opy_ is not None:
                bstack1lllll111ll_opy_[bstack11ll1ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᄚ")] = bstack1llll1l1lll_opy_
            if bstack1llll11l111_opy_ is not None and callable(getattr(bstack1llll11l111_opy_, bstack11ll1ll_opy_ (u"ࠦࡹࡵ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄛ"))):
                bstack1lllll111ll_opy_[bstack11ll1ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸࡥࡡࡴࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᄜ")] = bstack1llll11l111_opy_.to_capabilities()
        response = self.bstack1lllll11lll_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll111ll_opy_).encode(bstack11ll1ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᄝ")))
        if response is not None and response.capabilities:
            bstack1llllllll11_opy_ = json.loads(response.capabilities.decode(bstack11ll1ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᄞ")))
            if not bstack1llllllll11_opy_: # empty caps bstack1lllllll111_opy_ bstack1llllll111l_opy_ bstack1lllll1l111_opy_ bstack1llll111ll1_opy_ or error in processing
                return
            bstack1llll11ll11_opy_ = f.bstack1llll1ll1ll_opy_[bstack11ll1ll_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡩࡶࡴࡳ࡟ࡤࡣࡳࡷࠧᄟ")](bstack1llllllll11_opy_)
        if bstack1llll11l111_opy_ is not None and bstack1llll1l1l11_opy_ >= version.parse(bstack11ll1ll_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨᄠ")):
            bstack1lllll1l1l1_opy_ = None
        if (
                not bstack1llll11l111_opy_ and not bstack1llll1l1lll_opy_
        ) or (
                bstack1llll1l1l11_opy_ < version.parse(bstack11ll1ll_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᄡ"))
        ):
            bstack1lllll1l1l1_opy_ = {}
            bstack1lllll1l1l1_opy_.update(bstack1llllllll11_opy_)
        self.logger.info(bstack1lll1l11ll_opy_)
        if os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠢᄢ")).lower().__eq__(bstack11ll1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᄣ")):
            kwargs.update(
                {
                    bstack11ll1ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᄤ"): f.bstack1llll1l11l1_opy_,
                }
            )
        if bstack1llll1l1l11_opy_ >= version.parse(bstack11ll1ll_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧᄥ")):
            if bstack1llll1l1lll_opy_ is not None:
                del kwargs[bstack11ll1ll_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄦ")]
            kwargs.update(
                {
                    bstack11ll1ll_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᄧ"): bstack1llll11ll11_opy_,
                    bstack11ll1ll_opy_ (u"ࠥ࡯ࡪ࡫ࡰࡠࡣ࡯࡭ࡻ࡫ࠢᄨ"): True,
                    bstack11ll1ll_opy_ (u"ࠦ࡫࡯࡬ࡦࡡࡧࡩࡹ࡫ࡣࡵࡱࡵࠦᄩ"): None,
                }
            )
        elif bstack1llll1l1l11_opy_ >= version.parse(bstack11ll1ll_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᄪ")):
            kwargs.update(
                {
                    bstack11ll1ll_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄫ"): bstack1lllll1l1l1_opy_,
                    bstack11ll1ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡴࡴࡳࠣᄬ"): bstack1llll11ll11_opy_,
                    bstack11ll1ll_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧᄭ"): True,
                    bstack11ll1ll_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤᄮ"): None,
                }
            )
        elif bstack1llll1l1l11_opy_ >= version.parse(bstack11ll1ll_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪᄯ")):
            kwargs.update(
                {
                    bstack11ll1ll_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄰ"): bstack1lllll1l1l1_opy_,
                    bstack11ll1ll_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤᄱ"): True,
                    bstack11ll1ll_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨᄲ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11ll1ll_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄳ"): bstack1lllll1l1l1_opy_,
                    bstack11ll1ll_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧᄴ"): True,
                    bstack11ll1ll_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤᄵ"): None,
                }
            )