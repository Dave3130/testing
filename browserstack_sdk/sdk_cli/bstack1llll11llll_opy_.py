# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lllll111ll_opy_,
    bstack1llllll1l11_opy_,
    bstack1llll11l11l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll1l11l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1llll1l1ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1111l111l1_opy_ import bstack1lllllll111_opy_
class bstack1111111111_opy_(bstack1llllll111l_opy_):
    bstack1lllll1l111_opy_ = bstack11lll1_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦჇ")
    bstack1llll1l1lll_opy_ = bstack11lll1_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࠨ჈")
    bstack1llllllll11_opy_ = bstack11lll1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࠨ჉")
    def __init__(self, bstack1llll1l1111_opy_):
        super().__init__()
        bstack1lllll1l11l_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llllll1lll_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1lllll1lll1_opy_)
        bstack1lllll1l11l_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1lllll11ll1_opy_)
        bstack1lllll1l11l_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_, bstack1llllll1l11_opy_.POST), self.bstack1llll1ll1l1_opy_)
        bstack1lllll1l11l_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_, bstack1llllll1l11_opy_.POST), self.bstack1llllll11l1_opy_)
        bstack1lllll1l11l_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.QUIT, bstack1llllll1l11_opy_.POST), self.bstack1lllll1111l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1lll1_opy_(
        self,
        f: bstack1lllll1l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11lll1_opy_ (u"ࠢࡠࡡ࡬ࡲ࡮ࡺ࡟ࡠࠤ჊"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11lll1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦ჋")), str):
                    url = kwargs.get(bstack11lll1_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧ჌"))
                elif hasattr(kwargs.get(bstack11lll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨჍ")), bstack11lll1_opy_ (u"ࠫࡤࡩ࡬ࡪࡧࡱࡸࡤࡩ࡯࡯ࡨ࡬࡫ࠬ჎")):
                    url = kwargs.get(bstack11lll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣ჏"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11lll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤა"))._url
            except Exception as e:
                url = bstack11lll1_opy_ (u"ࠧࠨბ")
                self.logger.error(bstack11lll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡶࡴ࡯ࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࢂࠨგ").format(e))
            self.logger.info(bstack11lll1_opy_ (u"ࠤࡕࡩࡲࡵࡴࡦࠢࡖࡩࡷࡼࡥࡳࠢࡄࡨࡩࡸࡥࡴࡵࠣࡦࡪ࡯࡮ࡨࠢࡳࡥࡸࡹࡥࡥࠢࡤࡷࠥࡀࠠࡼࡿࠥდ").format(str(url)))
            self.bstack1lllllllll1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11lll1_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࢀࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࢃ࠺ࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࡻ࡬ࡹࡤࡶ࡬ࡹࡽࠣე").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1lllll11ll1_opy_(
        self,
        f: bstack1lllll1l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1111111111_opy_.bstack1lllll1l111_opy_, False):
            return
        if not f.bstack1llll1l11l1_opy_(instance, bstack1lllll1l11l_opy_.bstack1llll1ll111_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll1l11l_opy_.bstack1llll1ll111_opy_)
        if f.bstack1llll11l1ll_opy_(method_name, *args) and len(args) > 1:
            bstack11l11lll1l_opy_ = datetime.now()
            hub_url = bstack1lllll1l11l_opy_.hub_url(driver)
            self.logger.warning(bstack11lll1_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࡂࠨვ") + str(hub_url) + bstack11lll1_opy_ (u"ࠧࠨზ"))
            bstack1lllllll1l1_opy_ = args[1][bstack11lll1_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧთ")] if isinstance(args[1], dict) and bstack11lll1_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨი") in args[1] else None
            bstack1lllllll11l_opy_ = bstack11lll1_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨკ")
            if isinstance(bstack1lllllll1l1_opy_, dict):
                bstack11l11lll1l_opy_ = datetime.now()
                r = self.bstack1llllll11ll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺࠢლ"), datetime.now() - bstack11l11lll1l_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11lll1_opy_ (u"ࠥࡷࡴࡳࡥࡵࡪ࡬ࡲ࡬ࠦࡷࡦࡰࡷࠤࡼࡸ࡯࡯ࡩ࠽ࠤࠧმ") + str(r) + bstack11lll1_opy_ (u"ࠦࠧნ"))
                        return
                    if r.hub_url:
                        f.bstack1llllllllll_opy_(instance, driver, r.hub_url)
                        f.bstack1lllll11l11_opy_(instance, bstack1111111111_opy_.bstack1lllll1l111_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11lll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦო"), e)
    def bstack1llll1ll1l1_opy_(
        self,
        f: bstack1lllll1l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll1l11l_opy_.session_id(driver)
            if session_id:
                bstack1llll1llll1_opy_ = bstack11lll1_opy_ (u"ࠨࡻࡾ࠼ࡶࡸࡦࡸࡴࠣპ").format(session_id)
                bstack1lllllll111_opy_.mark(bstack1llll1llll1_opy_)
    def bstack1llllll11l1_opy_(
        self,
        f: bstack1lllll1l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1111111111_opy_.bstack1llll1l1lll_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll1l11l_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢ࡫ࡹࡧࡥࡵࡳ࡮ࡀࠦჟ") + str(hub_url) + bstack11lll1_opy_ (u"ࠣࠤრ"))
            return
        framework_session_id = bstack1lllll1l11l_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࡁࠧს") + str(framework_session_id) + bstack11lll1_opy_ (u"ࠥࠦტ"))
            return
        if bstack1lllll1l11l_opy_.bstack1llll11ll11_opy_(*args) == bstack1lllll1l11l_opy_.bstack1llll1lllll_opy_:
            bstack1lllll11l1l_opy_ = bstack11lll1_opy_ (u"ࠦࢀࢃ࠺ࡦࡰࡧࠦუ").format(framework_session_id)
            bstack1llll1llll1_opy_ = bstack11lll1_opy_ (u"ࠧࢁࡽ࠻ࡵࡷࡥࡷࡺࠢფ").format(framework_session_id)
            bstack1lllllll111_opy_.end(
                label=bstack11lll1_opy_ (u"ࠨࡳࡥ࡭࠽ࡨࡷ࡯ࡶࡦࡴ࠽ࡴࡴࡹࡴ࠮࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡥࡹ࡯࡯࡯ࠤქ"),
                start=bstack1llll1llll1_opy_,
                end=bstack1lllll11l1l_opy_,
                status=True,
                failure=None
            )
            bstack11l11lll1l_opy_ = datetime.now()
            r = self.bstack1llll11ll1l_opy_(
                ref,
                f.get_state(instance, bstack1lllll1l11l_opy_.bstack1llll1ll111_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡤࡶࡹࠨღ"), datetime.now() - bstack11l11lll1l_opy_)
            f.bstack1lllll11l11_opy_(instance, bstack1111111111_opy_.bstack1llll1l1lll_opy_, r.success)
    def bstack1lllll1111l_opy_(
        self,
        f: bstack1lllll1l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1111111111_opy_.bstack1llllllll11_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll1l11l_opy_.session_id(driver)
        hub_url = bstack1lllll1l11l_opy_.hub_url(driver)
        bstack11l11lll1l_opy_ = datetime.now()
        r = self.bstack1llll11l1l1_opy_(
            ref,
            f.get_state(instance, bstack1lllll1l11l_opy_.bstack1llll1ll111_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࠨყ"), datetime.now() - bstack11l11lll1l_opy_)
        f.bstack1lllll11l11_opy_(instance, bstack1111111111_opy_.bstack1llllllll11_opy_, r.success)
    @measure(event_name=EVENTS.bstack11l11lll11_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack1llllll1111_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11lll1_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢშ") + str(req) + bstack11lll1_opy_ (u"ࠥࠦჩ"))
        try:
            r = self.bstack1llll11lll1_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11lll1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࡹࡵࡤࡥࡨࡷࡸࡃࠢც") + str(r.success) + bstack11lll1_opy_ (u"ࠧࠨძ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦწ") + str(e) + bstack11lll1_opy_ (u"ࠢࠣჭ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll1ll1_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack1llllll11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llll1ll1ll_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack11lll1_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥხ") + str(req) + bstack11lll1_opy_ (u"ࠤࠥჯ"))
        try:
            r = self.bstack1llll11lll1_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11lll1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨჰ") + str(r.success) + bstack11lll1_opy_ (u"ࠦࠧჱ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥჲ") + str(e) + bstack11lll1_opy_ (u"ࠨࠢჳ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllllll1l_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack1llll11ll1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1ll1ll_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11lll1_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡࡶࡸࡦࡸࡴ࠻ࠢࠥჴ") + str(req) + bstack11lll1_opy_ (u"ࠣࠤჵ"))
        try:
            r = self.bstack1llll11lll1_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11lll1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦჶ") + str(r) + bstack11lll1_opy_ (u"ࠥࠦჷ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤჸ") + str(e) + bstack11lll1_opy_ (u"ࠧࠨჹ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll1l1l1l_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack1llll11l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1ll1ll_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack11lll1_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡳࡵࡀࠠࠣჺ") + str(req) + bstack11lll1_opy_ (u"ࠢࠣ჻"))
        try:
            r = self.bstack1llll11lll1_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11lll1_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥჼ") + str(r) + bstack11lll1_opy_ (u"ࠤࠥჽ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣჾ") + str(e) + bstack11lll1_opy_ (u"ࠦࠧჿ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lll11111l_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack1lllllllll1_opy_(self, instance: bstack1llll11l11l_opy_, url: str, f: bstack1lllll1l11l_opy_, kwargs):
        bstack111111111l_opy_ = version.parse(f.framework_version)
        bstack1lllll1ll11_opy_ = kwargs.get(bstack11lll1_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᄀ"))
        bstack1llll1l1l11_opy_ = kwargs.get(bstack11lll1_opy_ (u"ࠨࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᄁ"))
        bstack1llll1l11ll_opy_ = {}
        bstack1lllll11lll_opy_ = {}
        bstack1lllll1l1l1_opy_ = None
        bstack1lllll11111_opy_ = {}
        if bstack1llll1l1l11_opy_ is not None or bstack1lllll1ll11_opy_ is not None: # check top level caps
            if bstack1llll1l1l11_opy_ is not None:
                bstack1lllll11111_opy_[bstack11lll1_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᄂ")] = bstack1llll1l1l11_opy_
            if bstack1lllll1ll11_opy_ is not None and callable(getattr(bstack1lllll1ll11_opy_, bstack11lll1_opy_ (u"ࠣࡶࡲࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᄃ"))):
                bstack1lllll11111_opy_[bstack11lll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࡢࡥࡸࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᄄ")] = bstack1lllll1ll11_opy_.to_capabilities()
        response = self.bstack1llllll1111_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll11111_opy_).encode(bstack11lll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᄅ")))
        if response is not None and response.capabilities:
            bstack1llll1l11ll_opy_ = json.loads(response.capabilities.decode(bstack11lll1_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᄆ")))
            if not bstack1llll1l11ll_opy_: # empty caps bstack1lllllll1ll_opy_ bstack1lllll111l1_opy_ bstack11111111l1_opy_ bstack1llll1ll11l_opy_ or error in processing
                return
            bstack1lllll1l1l1_opy_ = f.bstack1llll1l111l_opy_[bstack11lll1_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡤࡵࡰࡵ࡫ࡲࡲࡸࡥࡦࡳࡱࡰࡣࡨࡧࡰࡴࠤᄇ")](bstack1llll1l11ll_opy_)
        if bstack1lllll1ll11_opy_ is not None and bstack111111111l_opy_ >= version.parse(bstack11lll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᄈ")):
            bstack1lllll11lll_opy_ = None
        if (
                not bstack1lllll1ll11_opy_ and not bstack1llll1l1l11_opy_
        ) or (
                bstack111111111l_opy_ < version.parse(bstack11lll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᄉ"))
        ):
            bstack1lllll11lll_opy_ = {}
            bstack1lllll11lll_opy_.update(bstack1llll1l11ll_opy_)
        self.logger.info(bstack1llll1l1ll_opy_)
        if os.environ.get(bstack11lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠦᄊ")).lower().__eq__(bstack11lll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᄋ")):
            kwargs.update(
                {
                    bstack11lll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᄌ"): f.bstack1lllll1l1ll_opy_,
                }
            )
        if bstack111111111l_opy_ >= version.parse(bstack11lll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫᄍ")):
            if bstack1llll1l1l11_opy_ is not None:
                del kwargs[bstack11lll1_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄎ")]
            kwargs.update(
                {
                    bstack11lll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡳࡳࡹࠢᄏ"): bstack1lllll1l1l1_opy_,
                    bstack11lll1_opy_ (u"ࠢ࡬ࡧࡨࡴࡤࡧ࡬ࡪࡸࡨࠦᄐ"): True,
                    bstack11lll1_opy_ (u"ࠣࡨ࡬ࡰࡪࡥࡤࡦࡶࡨࡧࡹࡵࡲࠣᄑ"): None,
                }
            )
        elif bstack111111111l_opy_ >= version.parse(bstack11lll1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨᄒ")):
            kwargs.update(
                {
                    bstack11lll1_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᄓ"): bstack1lllll11lll_opy_,
                    bstack11lll1_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᄔ"): bstack1lllll1l1l1_opy_,
                    bstack11lll1_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤᄕ"): True,
                    bstack11lll1_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨᄖ"): None,
                }
            )
        elif bstack111111111l_opy_ >= version.parse(bstack11lll1_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧᄗ")):
            kwargs.update(
                {
                    bstack11lll1_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄘ"): bstack1lllll11lll_opy_,
                    bstack11lll1_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᄙ"): True,
                    bstack11lll1_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᄚ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11lll1_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄛ"): bstack1lllll11lll_opy_,
                    bstack11lll1_opy_ (u"ࠧࡱࡥࡦࡲࡢࡥࡱ࡯ࡶࡦࠤᄜ"): True,
                    bstack11lll1_opy_ (u"ࠨࡦࡪ࡮ࡨࡣࡩ࡫ࡴࡦࡥࡷࡳࡷࠨᄝ"): None,
                }
            )