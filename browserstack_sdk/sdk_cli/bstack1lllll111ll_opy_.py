# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
    bstack1lllll111l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1111l11l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
class bstack1lllll1l1ll_opy_(bstack1lllll1111l_opy_):
    bstack11111111l1_opy_ = bstack1lllll1l_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴࠣ჋")
    bstack1lllll1ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥ჌")
    bstack1llll1l11ll_opy_ = bstack1lllll1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥჍ")
    def __init__(self, bstack1llllll1111_opy_):
        super().__init__()
        bstack1llll1lllll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11111_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1lllll11lll_opy_)
        bstack1llll1lllll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1llll1lll1l_opy_)
        bstack1llll1lllll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_, bstack1llllll1l11_opy_.POST), self.bstack111111111l_opy_)
        bstack1llll1lllll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_, bstack1llllll1l11_opy_.POST), self.bstack1llllll1l1l_opy_)
        bstack1llll1lllll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.QUIT, bstack1llllll1l11_opy_.POST), self.bstack1lllll1lll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll11lll_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lllll1l_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨ჎"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1lllll1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣ჏")), str):
                    url = kwargs.get(bstack1lllll1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤა"))
                elif hasattr(kwargs.get(bstack1lllll1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥბ")), bstack1lllll1l_opy_ (u"ࠨࡡࡦࡰ࡮࡫࡮ࡵࡡࡦࡳࡳ࡬ࡩࡨࠩგ")):
                    url = kwargs.get(bstack1lllll1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧდ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1lllll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨე"))._url
            except Exception as e:
                url = bstack1lllll1l_opy_ (u"ࠫࠬვ")
                self.logger.error(bstack1lllll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡺࡸ࡬ࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷࡀࠠࡼࡿࠥზ").format(e))
            self.logger.info(bstack1lllll1l_opy_ (u"ࠨࡒࡦ࡯ࡲࡸࡪࠦࡓࡦࡴࡹࡩࡷࠦࡁࡥࡦࡵࡩࡸࡹࠠࡣࡧ࡬ࡲ࡬ࠦࡰࡢࡵࡶࡩࡩࠦࡡࡴࠢ࠽ࠤࢀࢃࠢთ").format(str(url)))
            self.bstack1lllll1llll_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1lllll1l_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠮ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀ࠾ࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧი").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1llll1lll1l_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1lllll1l1ll_opy_.bstack11111111l1_opy_, False):
            return
        if not f.bstack1lllllll11l_opy_(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_):
            return
        platform_index = f.get_state(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_)
        if f.bstack1llll1l1ll1_opy_(method_name, *args) and len(args) > 1:
            bstack1ll111ll1_opy_ = datetime.now()
            hub_url = bstack1llll1lllll_opy_.hub_url(driver)
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭࠿ࠥკ") + str(hub_url) + bstack1lllll1l_opy_ (u"ࠤࠥლ"))
            bstack1llll1l1111_opy_ = args[1][bstack1lllll1l_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤმ")] if isinstance(args[1], dict) and bstack1lllll1l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥნ") in args[1] else None
            bstack1lllllllll1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥო")
            if isinstance(bstack1llll1l1111_opy_, dict):
                bstack1ll111ll1_opy_ = datetime.now()
                r = self.bstack1llll1l1l1l_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦპ"), datetime.now() - bstack1ll111ll1_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1lllll1l_opy_ (u"ࠢࡴࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭࠺ࠡࠤჟ") + str(r) + bstack1lllll1l_opy_ (u"ࠣࠤრ"))
                        return
                    if r.hub_url:
                        f.bstack1llll11llll_opy_(instance, driver, r.hub_url)
                        f.bstack1llll11ll1l_opy_(instance, bstack1lllll1l1ll_opy_.bstack11111111l1_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣს"), e)
    def bstack111111111l_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llll1lllll_opy_.session_id(driver)
            if session_id:
                bstack1llll11ll11_opy_ = bstack1lllll1l_opy_ (u"ࠥࡿࢂࡀࡳࡵࡣࡵࡸࠧტ").format(session_id)
                bstack1llllllll1l_opy_.mark(bstack1llll11ll11_opy_)
    def bstack1llllll1l1l_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llll1lllll_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣუ") + str(hub_url) + bstack1lllll1l_opy_ (u"ࠧࠨფ"))
            return
        framework_session_id = bstack1llll1lllll_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1lllll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤქ") + str(framework_session_id) + bstack1lllll1l_opy_ (u"ࠢࠣღ"))
            return
        if bstack1llll1lllll_opy_.bstack1llllllll11_opy_(*args) == bstack1llll1lllll_opy_.bstack1llllll11ll_opy_:
            bstack1llll1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠣࡽࢀ࠾ࡪࡴࡤࠣყ").format(framework_session_id)
            bstack1llll11ll11_opy_ = bstack1lllll1l_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦშ").format(framework_session_id)
            bstack1llllllll1l_opy_.end(
                label=bstack1lllll1l_opy_ (u"ࠥࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡱࡶࡸ࠲࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳࠨჩ"),
                start=bstack1llll11ll11_opy_,
                end=bstack1llll1ll1ll_opy_,
                status=True,
                failure=None
            )
            bstack1ll111ll1_opy_ = datetime.now()
            r = self.bstack1llll11l1l1_opy_(
                ref,
                f.get_state(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥც"), datetime.now() - bstack1ll111ll1_opy_)
            f.bstack1llll11ll1l_opy_(instance, bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_, r.success)
    def bstack1lllll1lll1_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1l1ll_opy_.bstack1llll1l11ll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llll1lllll_opy_.session_id(driver)
        hub_url = bstack1llll1lllll_opy_.hub_url(driver)
        bstack1ll111ll1_opy_ = datetime.now()
        r = self.bstack1llll1ll1l1_opy_(
            ref,
            f.get_state(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥძ"), datetime.now() - bstack1ll111ll1_opy_)
        f.bstack1llll11ll1l_opy_(instance, bstack1lllll1l1ll_opy_.bstack1llll1l11ll_opy_, r.success)
    @measure(event_name=EVENTS.bstack11lll1l1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1llllll111l_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦწ") + str(req) + bstack1lllll1l_opy_ (u"ࠢࠣჭ"))
        try:
            r = self.bstack1lllllll111_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦხ") + str(r.success) + bstack1lllll1l_opy_ (u"ࠤࠥჯ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣჰ") + str(e) + bstack1lllll1l_opy_ (u"ࠦࠧჱ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1111111111_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1llll1l1l1l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢჲ") + str(req) + bstack1lllll1l_opy_ (u"ࠨࠢჳ"))
        try:
            r = self.bstack1lllllll111_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥჴ") + str(r.success) + bstack1lllll1l_opy_ (u"ࠣࠤჵ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢჶ") + str(e) + bstack1lllll1l_opy_ (u"ࠥࠦჷ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll1ll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1llll11l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸ࠿ࠦࠢჸ") + str(req) + bstack1lllll1l_opy_ (u"ࠧࠨჹ"))
        try:
            r = self.bstack1lllllll111_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣჺ") + str(r) + bstack1lllll1l_opy_ (u"ࠢࠣ჻"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨჼ") + str(e) + bstack1lllll1l_opy_ (u"ࠤࠥჽ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llllll11l1_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1llll1ll1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲ࠽ࠤࠧჾ") + str(req) + bstack1lllll1l_opy_ (u"ࠦࠧჿ"))
        try:
            r = self.bstack1lllllll111_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᄀ") + str(r) + bstack1lllll1l_opy_ (u"ࠨࠢᄁ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᄂ") + str(e) + bstack1lllll1l_opy_ (u"ࠣࠤᄃ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1l111ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack1lllll1llll_opy_(self, instance: bstack1lllll111l1_opy_, url: str, f: bstack1llll1lllll_opy_, kwargs):
        bstack1lllll1l1l1_opy_ = version.parse(f.framework_version)
        bstack1lllll11l11_opy_ = kwargs.get(bstack1lllll1l_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᄄ"))
        bstack1lllllll1ll_opy_ = kwargs.get(bstack1lllll1l_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᄅ"))
        bstack1lllll1l11l_opy_ = {}
        bstack1llllll1lll_opy_ = {}
        bstack1llll1llll1_opy_ = None
        bstack1lllll1l111_opy_ = {}
        if bstack1lllllll1ll_opy_ is not None or bstack1lllll11l11_opy_ is not None: # check top level caps
            if bstack1lllllll1ll_opy_ is not None:
                bstack1lllll1l111_opy_[bstack1lllll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫᄆ")] = bstack1lllllll1ll_opy_
            if bstack1lllll11l11_opy_ is not None and callable(getattr(bstack1lllll11l11_opy_, bstack1lllll1l_opy_ (u"ࠧࡺ࡯ࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄇ"))):
                bstack1lllll1l111_opy_[bstack1lllll1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡢࡵࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᄈ")] = bstack1lllll11l11_opy_.to_capabilities()
        response = self.bstack1llllll111l_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll1l111_opy_).encode(bstack1lllll1l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᄉ")))
        if response is not None and response.capabilities:
            bstack1lllll1l11l_opy_ = json.loads(response.capabilities.decode(bstack1lllll1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᄊ")))
            if not bstack1lllll1l11l_opy_: # empty caps bstack1llll11l11l_opy_ bstack1llll11lll1_opy_ bstack1lllll1ll11_opy_ bstack1lllll11ll1_opy_ or error in processing
                return
            bstack1llll1llll1_opy_ = f.bstack1llll1ll11l_opy_[bstack1lllll1l_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨᄋ")](bstack1lllll1l11l_opy_)
        if bstack1lllll11l11_opy_ is not None and bstack1lllll1l1l1_opy_ >= version.parse(bstack1lllll1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᄌ")):
            bstack1llllll1lll_opy_ = None
        if (
                not bstack1lllll11l11_opy_ and not bstack1lllllll1ll_opy_
        ) or (
                bstack1lllll1l1l1_opy_ < version.parse(bstack1lllll1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪᄍ"))
        ):
            bstack1llllll1lll_opy_ = {}
            bstack1llllll1lll_opy_.update(bstack1lllll1l11l_opy_)
        self.logger.info(bstack1111l11l1_opy_)
        if os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣᄎ")).lower().__eq__(bstack1lllll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦᄏ")):
            kwargs.update(
                {
                    bstack1lllll1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᄐ"): f.bstack1llll1l111l_opy_,
                }
            )
        if bstack1lllll1l1l1_opy_ >= version.parse(bstack1lllll1l_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨᄑ")):
            if bstack1lllllll1ll_opy_ is not None:
                del kwargs[bstack1lllll1l_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄒ")]
            kwargs.update(
                {
                    bstack1lllll1l_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦᄓ"): bstack1llll1llll1_opy_,
                    bstack1lllll1l_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣᄔ"): True,
                    bstack1lllll1l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᄕ"): None,
                }
            )
        elif bstack1lllll1l1l1_opy_ >= version.parse(bstack1lllll1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᄖ")):
            kwargs.update(
                {
                    bstack1lllll1l_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄗ"): bstack1llllll1lll_opy_,
                    bstack1lllll1l_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᄘ"): bstack1llll1llll1_opy_,
                    bstack1lllll1l_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᄙ"): True,
                    bstack1lllll1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᄚ"): None,
                }
            )
        elif bstack1lllll1l1l1_opy_ >= version.parse(bstack1lllll1l_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫᄛ")):
            kwargs.update(
                {
                    bstack1lllll1l_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄜ"): bstack1llllll1lll_opy_,
                    bstack1lllll1l_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᄝ"): True,
                    bstack1lllll1l_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᄞ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1lllll1l_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄟ"): bstack1llllll1lll_opy_,
                    bstack1lllll1l_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᄠ"): True,
                    bstack1lllll1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᄡ"): None,
                }
            )