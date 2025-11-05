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
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11lll_opy_ import (
    bstack1111111111_opy_,
    bstack1llll1lllll_opy_,
    bstack1lllllll11l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l1111_opy_ import bstack1llllll1ll1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllllll1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11ll1l_opy_(bstack1lllllll1l1_opy_):
    bstack1l1ll11l1ll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llllll1ll1_opy_.bstack1lllll11111_opy_((bstack1111111111_opy_.bstack1llll1ll111_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1lllllll1ll_opy_)
    def is_enabled(self) -> bool:
        return True
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
        hub_url = f.hub_url(driver)
        if f.bstack1ll1lllll1l_opy_(hub_url):
            if not bstack1l1ll11ll1l_opy_.bstack1l1ll11l1ll_opy_:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠤ࡯ࡳࡨࡧ࡬ࠡࡵࡨࡰ࡫࠳ࡨࡦࡣ࡯ࠤ࡫ࡲ࡯ࡸࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡪࡰࡩࡶࡦࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥዠ") + str(hub_url) + bstack1lll11l_opy_ (u"ࠥࠦዡ"))
                bstack1l1ll11ll1l_opy_.bstack1l1ll11l1ll_opy_ = True
            return
        command_name = f.bstack1l1ll1ll1l1_opy_(*args)
        bstack1l1ll1l1l11_opy_ = f.bstack1l1lll1l111_opy_(*args)
        if command_name and command_name.lower() == bstack1lll11l_opy_ (u"ࠦ࡫࡯࡮ࡥࡧ࡯ࡩࡲ࡫࡮ࡵࠤዢ") and bstack1l1ll1l1l11_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1ll1l1l11_opy_.get(bstack1lll11l_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦዣ"), None), bstack1l1ll1l1l11_opy_.get(bstack1lll11l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧዤ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠢࡼࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࡽ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡺࡹࡩ࡯ࡩࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡼࡡ࡭ࡷࡨࡁࠧዥ") + str(locator_value) + bstack1lll11l_opy_ (u"ࠣࠤዦ"))
                return
            def bstack1l1ll11lll1_opy_(driver, bstack1l1ll11l1l1_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11l1l1_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll111ll1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1lll11l_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧዧ") + str(locator_value) + bstack1lll11l_opy_ (u"ࠥࠦየ"))
                    else:
                        self.logger.warning(bstack1lll11l_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢዩ") + str(response) + bstack1lll11l_opy_ (u"ࠧࠨዪ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll11l111_opy_(
                        driver, bstack1l1ll11l1l1_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll11lll1_opy_.__name__ = command_name
            return bstack1l1ll11lll1_opy_
    def __1l1ll11l111_opy_(
        self,
        driver,
        bstack1l1ll11l1l1_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll111ll1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1lll11l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡶࡵ࡭࡬࡭ࡥࡳࡧࡧ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨያ") + str(locator_value) + bstack1lll11l_opy_ (u"ࠢࠣዬ"))
                bstack1l1ll11ll11_opy_ = self.bstack1l1ll11l11l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1lll11l_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡨࡦࡣ࡯࡭ࡳ࡭࡟ࡳࡧࡶࡹࡱࡺ࠽ࠣይ") + str(bstack1l1ll11ll11_opy_) + bstack1lll11l_opy_ (u"ࠤࠥዮ"))
                if bstack1l1ll11ll11_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1lll11l_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤዯ"): bstack1l1ll11ll11_opy_.locator_type,
                            bstack1lll11l_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥደ"): bstack1l1ll11ll11_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11l1l1_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡏ࡟ࡅࡇࡅ࡙ࡌࠨዱ"), False):
                    self.logger.info(bstack1lll1ll1l11_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠮࡯࡬ࡷࡸ࡯࡮ࡨ࠼ࠣࡷࡱ࡫ࡥࡱࠪ࠶࠴࠮ࠦ࡬ࡦࡶࡷ࡭ࡳ࡭ࠠࡺࡱࡸࠤ࡮ࡴࡳࡱࡧࡦࡸࠥࡺࡨࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠦ࡬ࡰࡩࡶࠦዲ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1lll11l_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡰࡲ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠿ࠥዳ") + str(response) + bstack1lll11l_opy_ (u"ࠣࠤዴ"))
        except Exception as err:
            self.logger.warning(bstack1lll11l_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨድ") + str(err) + bstack1lll11l_opy_ (u"ࠥࠦዶ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll111lll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1l1ll111ll1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1lll11l_opy_ (u"ࠦ࠵ࠨዷ"),
    ):
        self.bstack1llllll1lll_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1lll11l_opy_ (u"ࠧࠨዸ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll11l11l_opy_.AISelfHealStep(req)
            self.logger.info(bstack1lll11l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣዹ") + str(r) + bstack1lll11l_opy_ (u"ࠢࠣዺ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨዻ") + str(e) + bstack1lll11l_opy_ (u"ࠤࠥዼ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll111l11_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1l1ll11l11l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1lll11l_opy_ (u"ࠥ࠴ࠧዽ")):
        self.bstack1llllll1lll_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll11l11l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1lll11l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨዾ") + str(r) + bstack1lll11l_opy_ (u"ࠧࠨዿ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦጀ") + str(e) + bstack1lll11l_opy_ (u"ࠢࠣጁ"))
            traceback.print_exc()
            raise e