# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lllllll11l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1ll111111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
class bstack1lllll1l1ll_opy_(bstack1lllllll1l1_opy_):
    bstack1lllll11l1l_opy_ = bstack1lll11l_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴࠣჄ")
    bstack1llllll1111_opy_ = bstack1lll11l_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥჅ")
    bstack1llllll11l1_opy_ = bstack1lll11l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥ჆")
    def __init__(self, bstack1llllllll1l_opy_):
        super().__init__()
        bstack1llllll1ll1_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1l1ll1_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1llll1lll1l_opy_)
        bstack1llllll1ll1_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1lllllll1ll_opy_)
        bstack1llllll1ll1_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.POST), self.bstack1lllll1lll1_opy_)
        bstack1llllll1ll1_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.POST), self.bstack1llllllll11_opy_)
        bstack1llllll1ll1_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.QUIT, bstack1llll1lllll_opy_.POST), self.bstack1llll1ll1l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1lll1l_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1lll11l_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨჇ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1lll11l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣ჈")), str):
                    url = kwargs.get(bstack1lll11l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤ჉"))
                elif hasattr(kwargs.get(bstack1lll11l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥ჊")), bstack1lll11l_opy_ (u"ࠨࡡࡦࡰ࡮࡫࡮ࡵࡡࡦࡳࡳ࡬ࡩࡨࠩ჋")):
                    url = kwargs.get(bstack1lll11l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧ჌"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1lll11l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨჍ"))._url
            except Exception as e:
                url = bstack1lll11l_opy_ (u"ࠫࠬ჎")
                self.logger.error(bstack1lll11l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡺࡸ࡬ࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷࡀࠠࡼࡿࠥ჏").format(e))
            self.logger.info(bstack1lll11l_opy_ (u"ࠨࡒࡦ࡯ࡲࡸࡪࠦࡓࡦࡴࡹࡩࡷࠦࡁࡥࡦࡵࡩࡸࡹࠠࡣࡧ࡬ࡲ࡬ࠦࡰࡢࡵࡶࡩࡩࠦࡡࡴࠢ࠽ࠤࢀࢃࠢა").format(str(url)))
            self.bstack1llll11l1l1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1lll11l_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠮ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀ࠾ࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧბ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1lllllll1ll_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1lllll1l1ll_opy_.bstack1lllll11l1l_opy_, False):
            return
        if not f.bstack1llll11ll11_opy_(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_):
            return
        platform_index = f.get_state(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_)
        if f.bstack1llllllllll_opy_(method_name, *args) and len(args) > 1:
            bstack11ll11l1l_opy_ = datetime.now()
            hub_url = bstack1llllll1ll1_opy_.hub_url(driver)
            self.logger.warning(bstack1lll11l_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭࠿ࠥგ") + str(hub_url) + bstack1lll11l_opy_ (u"ࠤࠥდ"))
            bstack1lllllll111_opy_ = args[1][bstack1lll11l_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤე")] if isinstance(args[1], dict) and bstack1lll11l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥვ") in args[1] else None
            bstack11111111l1_opy_ = bstack1lll11l_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥზ")
            if isinstance(bstack1lllllll111_opy_, dict):
                bstack11ll11l1l_opy_ = datetime.now()
                r = self.bstack1llll1l11ll_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦთ"), datetime.now() - bstack11ll11l1l_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1lll11l_opy_ (u"ࠢࡴࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭࠺ࠡࠤი") + str(r) + bstack1lll11l_opy_ (u"ࠣࠤკ"))
                        return
                    if r.hub_url:
                        f.bstack1llll1l111l_opy_(instance, driver, r.hub_url)
                        f.bstack1llll1ll11l_opy_(instance, bstack1lllll1l1ll_opy_.bstack1lllll11l1l_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1lll11l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣლ"), e)
    def bstack1lllll1lll1_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1llllll1ll1_opy_.session_id(driver)
            if session_id:
                bstack1lllll111ll_opy_ = bstack1lll11l_opy_ (u"ࠥࡿࢂࡀࡳࡵࡣࡵࡸࠧმ").format(session_id)
                bstack1llll1l1l1l_opy_.mark(bstack1lllll111ll_opy_)
    def bstack1llllllll11_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1l1ll_opy_.bstack1llllll1111_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1llllll1ll1_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣნ") + str(hub_url) + bstack1lll11l_opy_ (u"ࠧࠨო"))
            return
        framework_session_id = bstack1llllll1ll1_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤპ") + str(framework_session_id) + bstack1lll11l_opy_ (u"ࠢࠣჟ"))
            return
        if bstack1llllll1ll1_opy_.bstack1lllll1111l_opy_(*args) == bstack1llllll1ll1_opy_.bstack1llllll1l11_opy_:
            bstack1llll1llll1_opy_ = bstack1lll11l_opy_ (u"ࠣࡽࢀ࠾ࡪࡴࡤࠣრ").format(framework_session_id)
            bstack1lllll111ll_opy_ = bstack1lll11l_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦს").format(framework_session_id)
            bstack1llll1l1l1l_opy_.end(
                label=bstack1lll11l_opy_ (u"ࠥࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡱࡶࡸ࠲࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳࠨტ"),
                start=bstack1lllll111ll_opy_,
                end=bstack1llll1llll1_opy_,
                status=True,
                failure=None
            )
            bstack11ll11l1l_opy_ = datetime.now()
            r = self.bstack1lllll1llll_opy_(
                ref,
                f.get_state(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥუ"), datetime.now() - bstack11ll11l1l_opy_)
            f.bstack1llll1ll11l_opy_(instance, bstack1lllll1l1ll_opy_.bstack1llllll1111_opy_, r.success)
    def bstack1llll1ll1l1_opy_(
        self,
        f: bstack1llllll1ll1_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll11l_opy_, str],
        bstack1lllll1l111_opy_: Tuple[bstack1111111111_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1lllll1l1ll_opy_.bstack1llllll11l1_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1llllll1ll1_opy_.session_id(driver)
        hub_url = bstack1llllll1ll1_opy_.hub_url(driver)
        bstack11ll11l1l_opy_ = datetime.now()
        r = self.bstack1lllll1l1l1_opy_(
            ref,
            f.get_state(instance, bstack1llllll1ll1_opy_.bstack1lllllllll1_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥფ"), datetime.now() - bstack11ll11l1l_opy_)
        f.bstack1llll1ll11l_opy_(instance, bstack1lllll1l1ll_opy_.bstack1llllll11l1_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1l1ll1l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1llll1l11l1_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦქ") + str(req) + bstack1lll11l_opy_ (u"ࠢࠣღ"))
        try:
            r = self.bstack1llll11l11l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦყ") + str(r.success) + bstack1lll11l_opy_ (u"ࠤࠥშ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣჩ") + str(e) + bstack1lll11l_opy_ (u"ࠦࠧც"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll11lll1_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1llll1l11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1llllll1lll_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢძ") + str(req) + bstack1lll11l_opy_ (u"ࠨࠢწ"))
        try:
            r = self.bstack1llll11l11l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥჭ") + str(r.success) + bstack1lll11l_opy_ (u"ࠣࠤხ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢჯ") + str(e) + bstack1lll11l_opy_ (u"ࠥࠦჰ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll1l11l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1lllll1llll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllll1lll_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸ࠿ࠦࠢჱ") + str(req) + bstack1lll11l_opy_ (u"ࠧࠨჲ"))
        try:
            r = self.bstack1llll11l11l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣჳ") + str(r) + bstack1lll11l_opy_ (u"ࠢࠣჴ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨჵ") + str(e) + bstack1lll11l_opy_ (u"ࠤࠥჶ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll11l11_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1lllll1l1l1_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1llllll1lll_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1lll11l_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲ࠽ࠤࠧჷ") + str(req) + bstack1lll11l_opy_ (u"ࠦࠧჸ"))
        try:
            r = self.bstack1llll11l11l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢჹ") + str(r) + bstack1lll11l_opy_ (u"ࠨࠢჺ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ჻") + str(e) + bstack1lll11l_opy_ (u"ࠣࠤჼ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack111ll111l1_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1llll11l1l1_opy_(self, instance: bstack1lllllll11l_opy_, url: str, f: bstack1llllll1ll1_opy_, kwargs):
        bstack1llll1l1lll_opy_ = version.parse(f.framework_version)
        bstack1llll1ll1ll_opy_ = kwargs.get(bstack1lll11l_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥჽ"))
        bstack1llll11ll1l_opy_ = kwargs.get(bstack1lll11l_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥჾ"))
        bstack1llll1lll11_opy_ = {}
        bstack1llllll1l1l_opy_ = {}
        bstack1llllll111l_opy_ = None
        bstack1lllll1ll11_opy_ = {}
        if bstack1llll11ll1l_opy_ is not None or bstack1llll1ll1ll_opy_ is not None: # check top level caps
            if bstack1llll11ll1l_opy_ is not None:
                bstack1lllll1ll11_opy_[bstack1lll11l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫჿ")] = bstack1llll11ll1l_opy_
            if bstack1llll1ll1ll_opy_ is not None and callable(getattr(bstack1llll1ll1ll_opy_, bstack1lll11l_opy_ (u"ࠧࡺ࡯ࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄀ"))):
                bstack1lllll1ll11_opy_[bstack1lll11l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡢࡵࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᄁ")] = bstack1llll1ll1ll_opy_.to_capabilities()
        response = self.bstack1llll1l11l1_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll1ll11_opy_).encode(bstack1lll11l_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨᄂ")))
        if response is not None and response.capabilities:
            bstack1llll1lll11_opy_ = json.loads(response.capabilities.decode(bstack1lll11l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᄃ")))
            if not bstack1llll1lll11_opy_: # empty caps bstack111111111l_opy_ bstack1lllll111l1_opy_ bstack1llll11l1ll_opy_ bstack1lllll11ll1_opy_ or error in processing
                return
            bstack1llllll111l_opy_ = f.bstack1llll1l1l11_opy_[bstack1lll11l_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨᄄ")](bstack1llll1lll11_opy_)
        if bstack1llll1ll1ll_opy_ is not None and bstack1llll1l1lll_opy_ >= version.parse(bstack1lll11l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩᄅ")):
            bstack1llllll1l1l_opy_ = None
        if (
                not bstack1llll1ll1ll_opy_ and not bstack1llll11ll1l_opy_
        ) or (
                bstack1llll1l1lll_opy_ < version.parse(bstack1lll11l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪᄆ"))
        ):
            bstack1llllll1l1l_opy_ = {}
            bstack1llllll1l1l_opy_.update(bstack1llll1lll11_opy_)
        self.logger.info(bstack1ll111111_opy_)
        if os.environ.get(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣᄇ")).lower().__eq__(bstack1lll11l_opy_ (u"ࠨࡴࡳࡷࡨࠦᄈ")):
            kwargs.update(
                {
                    bstack1lll11l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᄉ"): f.bstack1llll11llll_opy_,
                }
            )
        if bstack1llll1l1lll_opy_ >= version.parse(bstack1lll11l_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨᄊ")):
            if bstack1llll11ll1l_opy_ is not None:
                del kwargs[bstack1lll11l_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄋ")]
            kwargs.update(
                {
                    bstack1lll11l_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦᄌ"): bstack1llllll111l_opy_,
                    bstack1lll11l_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣᄍ"): True,
                    bstack1lll11l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᄎ"): None,
                }
            )
        elif bstack1llll1l1lll_opy_ >= version.parse(bstack1lll11l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᄏ")):
            kwargs.update(
                {
                    bstack1lll11l_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄐ"): bstack1llllll1l1l_opy_,
                    bstack1lll11l_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᄑ"): bstack1llllll111l_opy_,
                    bstack1lll11l_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᄒ"): True,
                    bstack1lll11l_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᄓ"): None,
                }
            )
        elif bstack1llll1l1lll_opy_ >= version.parse(bstack1lll11l_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫᄔ")):
            kwargs.update(
                {
                    bstack1lll11l_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄕ"): bstack1llllll1l1l_opy_,
                    bstack1lll11l_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᄖ"): True,
                    bstack1lll11l_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᄗ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1lll11l_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᄘ"): bstack1llllll1l1l_opy_,
                    bstack1lll11l_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᄙ"): True,
                    bstack1lll11l_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᄚ"): None,
                }
            )