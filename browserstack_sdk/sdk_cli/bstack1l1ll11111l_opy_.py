# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import (
    bstack1lllll1l1ll_opy_,
    bstack1llllll11ll_opy_,
    bstack1llll1llll1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll11llll_opy_ import bstack1llll1l111l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll11ll11_opy_ import bstack1lllll11111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11l1ll_opy_(bstack1lllll11111_opy_):
    bstack1l1ll111l11_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llll1l111l_opy_.bstack1llllll1l1l_opy_((bstack1lllll1l1ll_opy_.bstack1lllll1ll1l_opy_, bstack1llllll11ll_opy_.PRE), self.bstack1llllll1l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllll1l11_opy_(
        self,
        f: bstack1llll1l111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1llll1_opy_, str],
        bstack1llll1ll1l1_opy_: Tuple[bstack1lllll1l1ll_opy_, bstack1llllll11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1llll1l1_opy_(hub_url):
            if not bstack1l1ll11l1ll_opy_.bstack1l1ll111l11_opy_:
                self.logger.warning(bstack11l11ll_opy_ (u"ࠥࡰࡴࡩࡡ࡭ࠢࡶࡩࡱ࡬࠭ࡩࡧࡤࡰࠥ࡬࡬ࡰࡹࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡ࡫ࡱࡪࡷࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠢ࡫ࡹࡧࡥࡵࡳ࡮ࡀࠦዶ") + str(hub_url) + bstack11l11ll_opy_ (u"ࠦࠧዷ"))
                bstack1l1ll11l1ll_opy_.bstack1l1ll111l11_opy_ = True
            return
        command_name = f.bstack1l1ll1l1lll_opy_(*args)
        bstack1l1lll11l1l_opy_ = f.bstack1l1ll1lll1l_opy_(*args)
        if command_name and command_name.lower() == bstack11l11ll_opy_ (u"ࠧ࡬ࡩ࡯ࡦࡨࡰࡪࡳࡥ࡯ࡶࠥዸ") and bstack1l1lll11l1l_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll11l1l_opy_.get(bstack11l11ll_opy_ (u"ࠨࡵࡴ࡫ࡱ࡫ࠧዹ"), None), bstack1l1lll11l1l_opy_.get(bstack11l11ll_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨዺ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11l11ll_opy_ (u"ࠣࡽࡦࡳࡲࡳࡡ࡯ࡦࡢࡲࡦࡳࡥࡾ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡻࡳࡪࡰࡪࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡵࡲࠡࡣࡵ࡫ࡸ࠴ࡶࡢ࡮ࡸࡩࡂࠨዻ") + str(locator_value) + bstack11l11ll_opy_ (u"ࠤࠥዼ"))
                return
            def bstack1l1ll111ll1_opy_(driver, bstack1l1ll111l1l_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll111l1l_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll11l1l1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11l11ll_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨዽ") + str(locator_value) + bstack11l11ll_opy_ (u"ࠦࠧዾ"))
                    else:
                        self.logger.warning(bstack11l11ll_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸ࠳࡮ࡰ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠽ࠣዿ") + str(response) + bstack11l11ll_opy_ (u"ࠨࠢጀ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1111l1_opy_(
                        driver, bstack1l1ll111l1l_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll111ll1_opy_.__name__ = command_name
            return bstack1l1ll111ll1_opy_
    def __1l1ll1111l1_opy_(
        self,
        driver,
        bstack1l1ll111l1l_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll11l1l1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11l11ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡷࡶ࡮࡭ࡧࡦࡴࡨࡨ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࠢጁ") + str(locator_value) + bstack11l11ll_opy_ (u"ࠣࠤጂ"))
                bstack1l1ll1111ll_opy_ = self.bstack1l1ll11l11l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11l11ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡩࡧࡤࡰ࡮ࡴࡧࡠࡴࡨࡷࡺࡲࡴ࠾ࠤጃ") + str(bstack1l1ll1111ll_opy_) + bstack11l11ll_opy_ (u"ࠥࠦጄ"))
                if bstack1l1ll1111ll_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11l11ll_opy_ (u"ࠦࡺࡹࡩ࡯ࡩࠥጅ"): bstack1l1ll1111ll_opy_.locator_type,
                            bstack11l11ll_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦጆ"): bstack1l1ll1111ll_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll111l1l_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11l11ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡉࡠࡆࡈࡆ࡚ࡍࠢጇ"), False):
                    self.logger.info(bstack11ll111l_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠯ࡰ࡭ࡸࡹࡩ࡯ࡩ࠽ࠤࡸࡲࡥࡦࡲࠫ࠷࠵࠯ࠠ࡭ࡧࡷࡸ࡮ࡴࡧࠡࡻࡲࡹࠥ࡯࡮ࡴࡲࡨࡧࡹࠦࡴࡩࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࠠ࡭ࡱࡪࡷࠧገ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11l11ll_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯ࡱࡳ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࡀࠦጉ") + str(response) + bstack11l11ll_opy_ (u"ࠤࠥጊ"))
        except Exception as err:
            self.logger.warning(bstack11l11ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠿ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢጋ") + str(err) + bstack11l11ll_opy_ (u"ࠦࠧጌ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll111lll_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def bstack1l1ll11l1l1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11l11ll_opy_ (u"ࠧ࠶ࠢግ"),
    ):
        self.bstack1llll11l1l1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11l11ll_opy_ (u"ࠨࠢጎ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll1l1ll1_opy_.AISelfHealStep(req)
            self.logger.info(bstack11l11ll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤጏ") + str(r) + bstack11l11ll_opy_ (u"ࠣࠤጐ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢ጑") + str(e) + bstack11l11ll_opy_ (u"ࠥࠦጒ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11l111_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
    def bstack1l1ll11l11l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11l11ll_opy_ (u"ࠦ࠵ࠨጓ")):
        self.bstack1llll11l1l1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll1l1ll1_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11l11ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢጔ") + str(r) + bstack11l11ll_opy_ (u"ࠨࠢጕ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ጖") + str(e) + bstack11l11ll_opy_ (u"ࠣࠤ጗"))
            traceback.print_exc()
            raise e