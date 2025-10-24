# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import (
    bstack1llllll111l_opy_,
    bstack1llll1l111l_opy_,
    bstack1llllll1l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1111111l11_opy_ import bstack1llll1l11l1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1lll1111l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack111l11l11_opy_ import bstack1lllllll11l_opy_
class bstack1llll11lll1_opy_(bstack1llll1llll1_opy_):
    bstack1111111111_opy_ = bstack1l1_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦჀ")
    bstack1llllllll1l_opy_ = bstack1l1_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࠨჁ")
    bstack1llll1ll1ll_opy_ = bstack1l1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࠨჂ")
    def __init__(self, bstack1lllll1llll_opy_):
        super().__init__()
        bstack1llll1l11l1_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllll1ll11_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1llll1lllll_opy_)
        bstack1llll1l11l1_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllllll111_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1lllll11ll1_opy_)
        bstack1llll1l11l1_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllllll111_opy_, bstack1llll1l111l_opy_.POST), self.bstack1llllll1111_opy_)
        bstack1llll1l11l1_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllllll111_opy_, bstack1llll1l111l_opy_.POST), self.bstack1lllll1l111_opy_)
        bstack1llll1l11l1_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.QUIT, bstack1llll1l111l_opy_.POST), self.bstack1lllll11l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1lllll_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1_opy_ (u"ࠢࡠࡡ࡬ࡲ࡮ࡺ࡟ࡠࠤჃ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦჄ")), str):
                    url = kwargs.get(bstack1l1_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧჅ"))
                elif hasattr(kwargs.get(bstack1l1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨ჆")), bstack1l1_opy_ (u"ࠫࡤࡩ࡬ࡪࡧࡱࡸࡤࡩ࡯࡯ࡨ࡬࡫ࠬჇ")):
                    url = kwargs.get(bstack1l1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣ჈"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1l1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤ჉"))._url
            except Exception as e:
                url = bstack1l1_opy_ (u"ࠧࠨ჊")
                self.logger.error(bstack1l1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡴ࡯ࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࢂࠨ჋").format(e))
            self.logger.info(bstack1l1_opy_ (u"ࠤࡕࡩࡲࡵࡴࡦࠢࡖࡩࡷࡼࡥࡳࠢࡄࡨࡩࡸࡥࡴࡵࠣࡦࡪ࡯࡮ࡨࠢࡳࡥࡸࡹࡥࡥࠢࡤࡷࠥࡀࠠࡼࡿࠥ჌").format(str(url)))
            self.bstack1lllllllll1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1l1_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࢀࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࢃ࠺ࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣჍ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1lllll11ll1_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llll11lll1_opy_.bstack1111111111_opy_, False):
            return
        if not f.bstack1llllllll11_opy_(instance, bstack1llll1l11l1_opy_.bstack1lllll1l11l_opy_):
            return
        platform_index = f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1l11l_opy_)
        if f.bstack1llll1ll11l_opy_(method_name, *args) and len(args) > 1:
            bstack1l1ll111l_opy_ = datetime.now()
            hub_url = bstack1llll1l11l1_opy_.hub_url(driver)
            self.logger.warning(bstack1l1_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࡂࠨ჎") + str(hub_url) + bstack1l1_opy_ (u"ࠧࠨ჏"))
            bstack1llll11ll11_opy_ = args[1][bstack1l1_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧა")] if isinstance(args[1], dict) and bstack1l1_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨბ") in args[1] else None
            bstack1llllll1l11_opy_ = bstack1l1_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨგ")
            if isinstance(bstack1llll11ll11_opy_, dict):
                bstack1l1ll111l_opy_ = datetime.now()
                r = self.bstack1lllll1111l_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺࠢდ"), datetime.now() - bstack1l1ll111l_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1l1_opy_ (u"ࠥࡷࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩ࠽ࠤࠧე") + str(r) + bstack1l1_opy_ (u"ࠦࠧვ"))
                        return
                    if r.hub_url:
                        f.bstack111111111l_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1l1lll_opy_(instance, bstack1llll11lll1_opy_.bstack1111111111_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1l1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦზ"), e)
    def bstack1llllll1111_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llll1l11l1_opy_.session_id(driver)
            if session_id:
                bstack1lllll111l1_opy_ = bstack1l1_opy_ (u"ࠨࡻࡾ࠼ࡶࡸࡦࡸࡴࠣთ").format(session_id)
                bstack1lllllll11l_opy_.mark(bstack1lllll111l1_opy_)
    def bstack1lllll1l111_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11lll1_opy_.bstack1llllllll1l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llll1l11l1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢ࡫ࡹࡧࡥࡵࡳ࡮ࡀࠦი") + str(hub_url) + bstack1l1_opy_ (u"ࠣࠤკ"))
            return
        framework_session_id = bstack1llll1l11l1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࡁࠧლ") + str(framework_session_id) + bstack1l1_opy_ (u"ࠥࠦმ"))
            return
        if bstack1llll1l11l1_opy_.bstack1llll1l1ll1_opy_(*args) == bstack1llll1l11l1_opy_.bstack1llllllllll_opy_:
            bstack1lllllll1ll_opy_ = bstack1l1_opy_ (u"ࠦࢀࢃ࠺ࡦࡰࡧࠦნ").format(framework_session_id)
            bstack1lllll111l1_opy_ = bstack1l1_opy_ (u"ࠧࢁࡽ࠻ࡵࡷࡥࡷࡺࠢო").format(framework_session_id)
            bstack1lllllll11l_opy_.end(
                label=bstack1l1_opy_ (u"ࠨࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡴࡴࡹࡴ࠮࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠤპ"),
                start=bstack1lllll111l1_opy_,
                end=bstack1lllllll1ll_opy_,
                status=True,
                failure=None
            )
            bstack1l1ll111l_opy_ = datetime.now()
            r = self.bstack1llllll11ll_opy_(
                ref,
                f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1l11l_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࠨჟ"), datetime.now() - bstack1l1ll111l_opy_)
            f.bstack1llll1l1lll_opy_(instance, bstack1llll11lll1_opy_.bstack1llllllll1l_opy_, r.success)
    def bstack1lllll11l11_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll11lll1_opy_.bstack1llll1ll1ll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llll1l11l1_opy_.session_id(driver)
        hub_url = bstack1llll1l11l1_opy_.hub_url(driver)
        bstack1l1ll111l_opy_ = datetime.now()
        r = self.bstack1lllll1lll1_opy_(
            ref,
            f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1l11l_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࠨრ"), datetime.now() - bstack1l1ll111l_opy_)
        f.bstack1llll1l1lll_opy_(instance, bstack1llll11lll1_opy_.bstack1llll1ll1ll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1111l11l1l_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack11111111ll_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1l1_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢს") + str(req) + bstack1l1_opy_ (u"ࠥࠦტ"))
        try:
            r = self.bstack1llll1l11ll_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢუ") + str(r.success) + bstack1l1_opy_ (u"ࠧࠨფ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦქ") + str(e) + bstack1l1_opy_ (u"ࠢࠣღ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11lll_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1lllll1111l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llll1l1l1l_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1l1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥყ") + str(req) + bstack1l1_opy_ (u"ࠤࠥშ"))
        try:
            r = self.bstack1llll1l11ll_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨჩ") + str(r.success) + bstack1l1_opy_ (u"ࠦࠧც"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥძ") + str(e) + bstack1l1_opy_ (u"ࠨࠢწ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll1ll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1llllll11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1l1l1l_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴ࠻ࠢࠥჭ") + str(req) + bstack1l1_opy_ (u"ࠣࠤხ"))
        try:
            r = self.bstack1llll1l11ll_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦჯ") + str(r) + bstack1l1_opy_ (u"ࠥࠦჰ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤჱ") + str(e) + bstack1l1_opy_ (u"ࠧࠨჲ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1lll1l_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1lllll1lll1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1l1l1l_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࡀࠠࠣჳ") + str(req) + bstack1l1_opy_ (u"ࠢࠣჴ"))
        try:
            r = self.bstack1llll1l11ll_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1l1_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥჵ") + str(r) + bstack1l1_opy_ (u"ࠤࠥჶ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣჷ") + str(e) + bstack1l1_opy_ (u"ࠦࠧჸ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11l1111l1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1lllllllll1_opy_(self, instance: bstack1llllll1l1l_opy_, url: str, f: bstack1llll1l11l1_opy_, kwargs):
        bstack1111111l1l_opy_ = version.parse(f.framework_version)
        bstack1lllllll1l1_opy_ = kwargs.get(bstack1l1_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨჹ"))
        bstack1llllll11l1_opy_ = kwargs.get(bstack1l1_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨჺ"))
        bstack1lllll11111_opy_ = {}
        bstack1lllll111ll_opy_ = {}
        bstack11111111l1_opy_ = None
        bstack1llll11llll_opy_ = {}
        if bstack1llllll11l1_opy_ is not None or bstack1lllllll1l1_opy_ is not None: # check top level caps
            if bstack1llllll11l1_opy_ is not None:
                bstack1llll11llll_opy_[bstack1l1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ჻")] = bstack1llllll11l1_opy_
            if bstack1lllllll1l1_opy_ is not None and callable(getattr(bstack1lllllll1l1_opy_, bstack1l1_opy_ (u"ࠣࡶࡲࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥჼ"))):
                bstack1llll11llll_opy_[bstack1l1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࡢࡥࡸࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬჽ")] = bstack1lllllll1l1_opy_.to_capabilities()
        response = self.bstack11111111ll_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1llll11llll_opy_).encode(bstack1l1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤჾ")))
        if response is not None and response.capabilities:
            bstack1lllll11111_opy_ = json.loads(response.capabilities.decode(bstack1l1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥჿ")))
            if not bstack1lllll11111_opy_: # empty caps bstack1lllll1ll1l_opy_ bstack1lllll1l1ll_opy_ bstack1llll1l1111_opy_ bstack1llll1ll111_opy_ or error in processing
                return
            bstack11111111l1_opy_ = f.bstack1lllll11l1l_opy_[bstack1l1_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡤࡵࡰࡵ࡫ࡲࡲࡸࡥࡦࡳࡱࡰࡣࡨࡧࡰࡴࠤᄀ")](bstack1lllll11111_opy_)
        if bstack1lllllll1l1_opy_ is not None and bstack1111111l1l_opy_ >= version.parse(bstack1l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᄁ")):
            bstack1lllll111ll_opy_ = None
        if (
                not bstack1lllllll1l1_opy_ and not bstack1llllll11l1_opy_
        ) or (
                bstack1111111l1l_opy_ < version.parse(bstack1l1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᄂ"))
        ):
            bstack1lllll111ll_opy_ = {}
            bstack1lllll111ll_opy_.update(bstack1lllll11111_opy_)
        self.logger.info(bstack1lll1111l1_opy_)
        if os.environ.get(bstack1l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠦᄃ")).lower().__eq__(bstack1l1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᄄ")):
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᄅ"): f.bstack1llll1l1l11_opy_,
                }
            )
        if bstack1111111l1l_opy_ >= version.parse(bstack1l1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫᄆ")):
            if bstack1llllll11l1_opy_ is not None:
                del kwargs[bstack1l1_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄇ")]
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᄈ"): bstack11111111l1_opy_,
                    bstack1l1_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᄉ"): True,
                    bstack1l1_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᄊ"): None,
                }
            )
        elif bstack1111111l1l_opy_ >= version.parse(bstack1l1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨᄋ")):
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᄌ"): bstack1lllll111ll_opy_,
                    bstack1l1_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᄍ"): bstack11111111l1_opy_,
                    bstack1l1_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤᄎ"): True,
                    bstack1l1_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨᄏ"): None,
                }
            )
        elif bstack1111111l1l_opy_ >= version.parse(bstack1l1_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧᄐ")):
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄑ"): bstack1lllll111ll_opy_,
                    bstack1l1_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᄒ"): True,
                    bstack1l1_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᄓ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1l1_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄔ"): bstack1lllll111ll_opy_,
                    bstack1l1_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤᄕ"): True,
                    bstack1l1_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨᄖ"): None,
                }
            )