# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1llll1l1111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack111lll1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
class bstack1llll1l1l1l_opy_(bstack1llll1l1l11_opy_):
    bstack1lllll1ll1l_opy_ = bstack11l111_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤ࡯࡮ࡪࡶࠥჍ")
    bstack111111111l_opy_ = bstack11l111_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸࠧ჎")
    bstack1llllll1lll_opy_ = bstack11l111_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴࠧ჏")
    def __init__(self, bstack1llll1lllll_opy_):
        super().__init__()
        bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llll11llll_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1lllll11lll_opy_)
        bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1llllll1111_opy_)
        bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.POST), self.bstack1lllllll111_opy_)
        bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.POST), self.bstack1llll1ll1l1_opy_)
        bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.QUIT, bstack1llll1l1lll_opy_.POST), self.bstack11111111l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll11lll_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack11l111_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣა"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack11l111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥბ")), str):
                    url = kwargs.get(bstack11l111_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦგ"))
                elif hasattr(kwargs.get(bstack11l111_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧდ")), bstack11l111_opy_ (u"ࠪࡣࡨࡲࡩࡦࡰࡷࡣࡨࡵ࡮ࡧ࡫ࡪࠫე")):
                    url = kwargs.get(bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢვ"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack11l111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣზ"))._url
            except Exception as e:
                url = bstack11l111_opy_ (u"࠭ࠧთ")
                self.logger.error(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡵࡳ࡮ࠣࡪࡷࡵ࡭ࠡࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࢁࠧი").format(e))
            self.logger.info(bstack11l111_opy_ (u"ࠣࡔࡨࡱࡴࡺࡥࠡࡕࡨࡶࡻ࡫ࡲࠡࡃࡧࡨࡷ࡫ࡳࡴࠢࡥࡩ࡮ࡴࡧࠡࡲࡤࡷࡸ࡫ࡤࠡࡣࡶࠤ࠿ࠦࡻࡾࠤკ").format(str(url)))
            self.bstack1lllllllll1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack11l111_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࡀࡿࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࢂࡀࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢლ").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
    def bstack1llllll1111_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if f.get_state(instance, bstack1llll1l1l1l_opy_.bstack1lllll1ll1l_opy_, False):
            return
        if not f.bstack1lllllll1ll_opy_(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_):
            return
        platform_index = f.get_state(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_)
        if f.bstack1lllll1l11l_opy_(method_name, *args) and len(args) > 1:
            bstack1l1ll1ll1_opy_ = datetime.now()
            hub_url = bstack1lllll11l1l_opy_.hub_url(driver)
            self.logger.warning(bstack11l111_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧმ") + str(hub_url) + bstack11l111_opy_ (u"ࠦࠧნ"))
            bstack1lllll1111l_opy_ = args[1][bstack11l111_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦო")] if isinstance(args[1], dict) and bstack11l111_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧპ") in args[1] else None
            bstack1lllll1l1l1_opy_ = bstack11l111_opy_ (u"ࠢࡢ࡮ࡺࡥࡾࡹࡍࡢࡶࡦ࡬ࠧჟ")
            if isinstance(bstack1lllll1111l_opy_, dict):
                bstack1l1ll1ll1_opy_ = datetime.now()
                r = self.bstack1llll1l1ll1_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠ࡫ࡱ࡭ࡹࠨრ"), datetime.now() - bstack1l1ll1ll1_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack11l111_opy_ (u"ࠤࡶࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡽࡥ࡯ࡶࠣࡻࡷࡵ࡮ࡨ࠼ࠣࠦს") + str(r) + bstack11l111_opy_ (u"ࠥࠦტ"))
                        return
                    if r.hub_url:
                        f.bstack1lllll1llll_opy_(instance, driver, r.hub_url)
                        f.bstack1llllllll1l_opy_(instance, bstack1llll1l1l1l_opy_.bstack1lllll1ll1l_opy_, True)
                except Exception as e:
                    self.logger.error(bstack11l111_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥუ"), e)
    def bstack1lllllll111_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lllll11l1l_opy_.session_id(driver)
            if session_id:
                bstack1llllll111l_opy_ = bstack11l111_opy_ (u"ࠧࢁࡽ࠻ࡵࡷࡥࡷࡺࠢფ").format(session_id)
                bstack1llll11ll11_opy_.mark(bstack1llllll111l_opy_)
    def bstack1llll1ll1l1_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll1l1l1l_opy_.bstack111111111l_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lllll11l1l_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack11l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥქ") + str(hub_url) + bstack11l111_opy_ (u"ࠢࠣღ"))
            return
        framework_session_id = bstack1lllll11l1l_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack11l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦყ") + str(framework_session_id) + bstack11l111_opy_ (u"ࠤࠥშ"))
            return
        if bstack1lllll11l1l_opy_.bstack1llllll11ll_opy_(*args) == bstack1lllll11l1l_opy_.bstack1llll11l1ll_opy_:
            bstack1llll1ll1ll_opy_ = bstack11l111_opy_ (u"ࠥࡿࢂࡀࡥ࡯ࡦࠥჩ").format(framework_session_id)
            bstack1llllll111l_opy_ = bstack11l111_opy_ (u"ࠦࢀࢃ࠺ࡴࡶࡤࡶࡹࠨც").format(framework_session_id)
            bstack1llll11ll11_opy_.end(
                label=bstack11l111_opy_ (u"ࠧࡹࡤ࡬࠼ࡧࡶ࡮ࡼࡥࡳ࠼ࡳࡳࡸࡺ࠭ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡤࡸ࡮ࡵ࡮ࠣძ"),
                start=bstack1llllll111l_opy_,
                end=bstack1llll1ll1ll_opy_,
                status=True,
                failure=None
            )
            bstack1l1ll1ll1_opy_ = datetime.now()
            r = self.bstack1llll11l11l_opy_(
                ref,
                f.get_state(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸࠧწ"), datetime.now() - bstack1l1ll1ll1_opy_)
            f.bstack1llllllll1l_opy_(instance, bstack1llll1l1l1l_opy_.bstack111111111l_opy_, r.success)
    def bstack11111111l1_opy_(
        self,
        f: bstack1lllll11l1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.get_state(instance, bstack1llll1l1l1l_opy_.bstack1llllll1lll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lllll11l1l_opy_.session_id(driver)
        hub_url = bstack1lllll11l1l_opy_.hub_url(driver)
        bstack1l1ll1ll1_opy_ = datetime.now()
        r = self.bstack1llll11lll1_opy_(
            ref,
            f.get_state(instance, bstack1lllll11l1l_opy_.bstack1llllllll11_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴࠧჭ"), datetime.now() - bstack1l1ll1ll1_opy_)
        f.bstack1llllllll1l_opy_(instance, bstack1llll1l1l1l_opy_.bstack1llllll1lll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1ll1l1ll11_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1llll1l111l_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack11l111_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢࡻࡪࡨࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࠾ࠥࠨხ") + str(req) + bstack11l111_opy_ (u"ࠤࠥჯ"))
        try:
            r = self.bstack1llllll1l11_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࡸࡻࡣࡤࡧࡶࡷࡂࠨჰ") + str(r.success) + bstack11l111_opy_ (u"ࠦࠧჱ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥჲ") + str(e) + bstack11l111_opy_ (u"ࠨࠢჳ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll111l1_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1llll1l1ll1_opy_(
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
        self.logger.debug(bstack11l111_opy_ (u"ࠢࡳࡧࡪ࡭ࡸࡺࡥࡳࡡ࡬ࡲ࡮ࡺ࠺ࠡࠤჴ") + str(req) + bstack11l111_opy_ (u"ࠣࠤჵ"))
        try:
            r = self.bstack1llllll1l11_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࡷࡺࡩࡣࡦࡵࡶࡁࠧჶ") + str(r.success) + bstack11l111_opy_ (u"ࠥࠦჷ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤჸ") + str(e) + bstack11l111_opy_ (u"ࠧࠨჹ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lllll111ll_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1llll11l11l_opy_(
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
        self.logger.debug(bstack11l111_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡵࡷࡥࡷࡺ࠺ࠡࠤჺ") + str(req) + bstack11l111_opy_ (u"ࠢࠣ჻"))
        try:
            r = self.bstack1llllll1l11_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥჼ") + str(r) + bstack11l111_opy_ (u"ࠤࠥჽ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣჾ") + str(e) + bstack11l111_opy_ (u"ࠦࠧჿ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1llll11ll1l_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1llll11lll1_opy_(
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
        self.logger.debug(bstack11l111_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡴࡶࡲࡴ࠿ࠦࠢᄀ") + str(req) + bstack11l111_opy_ (u"ࠨࠢᄁ"))
        try:
            r = self.bstack1llllll1l11_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤᄂ") + str(r) + bstack11l111_opy_ (u"ࠣࠤᄃ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᄄ") + str(e) + bstack11l111_opy_ (u"ࠥࠦᄅ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll1111ll1_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1lllllllll1_opy_(self, instance: bstack1llll1l1111_opy_, url: str, f: bstack1lllll11l1l_opy_, kwargs):
        bstack1llll1lll1l_opy_ = version.parse(f.framework_version)
        bstack1llll1l11l1_opy_ = kwargs.get(bstack11l111_opy_ (u"ࠦࡴࡶࡴࡪࡱࡱࡷࠧᄆ"))
        bstack1lllllll1l1_opy_ = kwargs.get(bstack11l111_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᄇ"))
        bstack1lllll11111_opy_ = {}
        bstack1lllll1l111_opy_ = {}
        bstack1llll1llll1_opy_ = None
        bstack1lllll11ll1_opy_ = {}
        if bstack1lllllll1l1_opy_ is not None or bstack1llll1l11l1_opy_ is not None: # check top level caps
            if bstack1lllllll1l1_opy_ is not None:
                bstack1lllll11ll1_opy_[bstack11l111_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᄈ")] = bstack1lllllll1l1_opy_
            if bstack1llll1l11l1_opy_ is not None and callable(getattr(bstack1llll1l11l1_opy_, bstack11l111_opy_ (u"ࠢࡵࡱࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄉ"))):
                bstack1lllll11ll1_opy_[bstack11l111_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࡡࡤࡷࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫᄊ")] = bstack1llll1l11l1_opy_.to_capabilities()
        response = self.bstack1llll1l111l_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1lllll11ll1_opy_).encode(bstack11l111_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᄋ")))
        if response is not None and response.capabilities:
            bstack1lllll11111_opy_ = json.loads(response.capabilities.decode(bstack11l111_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤᄌ")))
            if not bstack1lllll11111_opy_: # empty caps bstack1llll1l11ll_opy_ bstack1111111111_opy_ bstack1llllllllll_opy_ bstack1llll11l1l1_opy_ or error in processing
                return
            bstack1llll1llll1_opy_ = f.bstack1llllll1ll1_opy_[bstack11l111_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡣࡴࡶࡴࡪࡱࡱࡷࡤ࡬ࡲࡰ࡯ࡢࡧࡦࡶࡳࠣᄍ")](bstack1lllll11111_opy_)
        if bstack1llll1l11l1_opy_ is not None and bstack1llll1lll1l_opy_ >= version.parse(bstack11l111_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᄎ")):
            bstack1lllll1l111_opy_ = None
        if (
                not bstack1llll1l11l1_opy_ and not bstack1lllllll1l1_opy_
        ) or (
                bstack1llll1lll1l_opy_ < version.parse(bstack11l111_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᄏ"))
        ):
            bstack1lllll1l111_opy_ = {}
            bstack1lllll1l111_opy_.update(bstack1lllll11111_opy_)
        self.logger.info(bstack111lll1l1_opy_)
        if os.environ.get(bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠥᄐ")).lower().__eq__(bstack11l111_opy_ (u"ࠣࡶࡵࡹࡪࠨᄑ")):
            kwargs.update(
                {
                    bstack11l111_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᄒ"): f.bstack1lllll11l11_opy_,
                }
            )
        if bstack1llll1lll1l_opy_ >= version.parse(bstack11l111_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪᄓ")):
            if bstack1lllllll1l1_opy_ is not None:
                del kwargs[bstack11l111_opy_ (u"ࠦࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᄔ")]
            kwargs.update(
                {
                    bstack11l111_opy_ (u"ࠧࡵࡰࡵ࡫ࡲࡲࡸࠨᄕ"): bstack1llll1llll1_opy_,
                    bstack11l111_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᄖ"): True,
                    bstack11l111_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᄗ"): None,
                }
            )
        elif bstack1llll1lll1l_opy_ >= version.parse(bstack11l111_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧᄘ")):
            kwargs.update(
                {
                    bstack11l111_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᄙ"): bstack1lllll1l111_opy_,
                    bstack11l111_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦᄚ"): bstack1llll1llll1_opy_,
                    bstack11l111_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣᄛ"): True,
                    bstack11l111_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᄜ"): None,
                }
            )
        elif bstack1llll1lll1l_opy_ >= version.parse(bstack11l111_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ᄝ")):
            kwargs.update(
                {
                    bstack11l111_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᄞ"): bstack1lllll1l111_opy_,
                    bstack11l111_opy_ (u"ࠣ࡭ࡨࡩࡵࡥࡡ࡭࡫ࡹࡩࠧᄟ"): True,
                    bstack11l111_opy_ (u"ࠤࡩ࡭ࡱ࡫࡟ࡥࡧࡷࡩࡨࡺ࡯ࡳࠤᄠ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack11l111_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᄡ"): bstack1lllll1l111_opy_,
                    bstack11l111_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣᄢ"): True,
                    bstack11l111_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᄣ"): None,
                }
            )