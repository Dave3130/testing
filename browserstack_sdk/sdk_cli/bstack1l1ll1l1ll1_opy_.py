# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
    bstack111111l111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1lllll1ll1l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1llll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1ll11l_opy_(bstack1llll1llll1_opy_):
    bstack1l1ll1l1l1l_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll1ll1l_opy_.bstack1lllll1111l_opy_((bstack1111111l11_opy_.bstack1111111ll1_opy_, bstack1llllll1ll1_opy_.PRE), self.bstack1111111111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1111111111_opy_(
        self,
        f: bstack1lllll1ll1l_opy_,
        driver: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll1111lll_opy_(hub_url):
            if not bstack1l1ll1ll11l_opy_.bstack1l1ll1l1l1l_opy_:
                self.logger.warning(bstack1l_opy_ (u"ࠢ࡭ࡱࡦࡥࡱࠦࡳࡦ࡮ࡩ࠱࡭࡫ࡡ࡭ࠢࡩࡰࡴࡽࠠࡥ࡫ࡶࡥࡧࡲࡥࡥࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥ࡯࡮ࡧࡴࡤࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣዉ") + str(hub_url) + bstack1l_opy_ (u"ࠣࠤዊ"))
                bstack1l1ll1ll11l_opy_.bstack1l1ll1l1l1l_opy_ = True
            return
        command_name = f.bstack1l1llll11l1_opy_(*args)
        bstack1l1lll11111_opy_ = f.bstack1l1lll1ll11_opy_(*args)
        if command_name and command_name.lower() == bstack1l_opy_ (u"ࠤࡩ࡭ࡳࡪࡥ࡭ࡧࡰࡩࡳࡺࠢዋ") and bstack1l1lll11111_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll11111_opy_.get(bstack1l_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤዌ"), None), bstack1l1lll11111_opy_.get(bstack1l_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥው"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1l_opy_ (u"ࠧࢁࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࢂࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡱࡵࠤࡦࡸࡧࡴ࠰ࡸࡷ࡮ࡴࡧ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢࡲࡶࠥࡧࡲࡨࡵ࠱ࡺࡦࡲࡵࡦ࠿ࠥዎ") + str(locator_value) + bstack1l_opy_ (u"ࠨࠢዏ"))
                return
            def bstack1l1ll1l1l11_opy_(driver, bstack1l1ll1ll111_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll1ll111_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll1ll1l1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1l_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳ࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࠥዐ") + str(locator_value) + bstack1l_opy_ (u"ࠣࠤዑ"))
                    else:
                        self.logger.warning(bstack1l_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡲࡴ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࡁࠧዒ") + str(response) + bstack1l_opy_ (u"ࠥࠦዓ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1l111l_opy_(
                        driver, bstack1l1ll1ll111_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1l1l11_opy_.__name__ = command_name
            return bstack1l1ll1l1l11_opy_
    def __1l1ll1l111l_opy_(
        self,
        driver,
        bstack1l1ll1ll111_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll1ll1l1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡴࡳ࡫ࡪ࡫ࡪࡸࡥࡥ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࠦዔ") + str(locator_value) + bstack1l_opy_ (u"ࠧࠨዕ"))
                bstack1l1ll1l1lll_opy_ = self.bstack1l1ll1l1111_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤ࡭࡫ࡡ࡭࡫ࡱ࡫ࡤࡸࡥࡴࡷ࡯ࡸࡂࠨዖ") + str(bstack1l1ll1l1lll_opy_) + bstack1l_opy_ (u"ࠢࠣ዗"))
                if bstack1l1ll1l1lll_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1l_opy_ (u"ࠣࡷࡶ࡭ࡳ࡭ࠢዘ"): bstack1l1ll1l1lll_opy_.locator_type,
                            bstack1l_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣዙ"): bstack1l1ll1l1lll_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1ll111_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡍࡤࡊࡅࡃࡗࡊࠦዚ"), False):
                    self.logger.info(bstack1lll1ll1l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹ࠳࡭ࡪࡵࡶ࡭ࡳ࡭࠺ࠡࡵ࡯ࡩࡪࡶࠨ࠴࠲ࠬࠤࡱ࡫ࡴࡵ࡫ࡱ࡫ࠥࡿ࡯ࡶࠢ࡬ࡲࡸࡶࡥࡤࡶࠣࡸ࡭࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡧࡻࡸࡪࡴࡳࡪࡱࡱࠤࡱࡵࡧࡴࠤዛ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳࡮ࡰ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠽ࠣዜ") + str(response) + bstack1l_opy_ (u"ࠨࠢዝ"))
        except Exception as err:
            self.logger.warning(bstack1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠼ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠦዞ") + str(err) + bstack1l_opy_ (u"ࠣࠤዟ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll1l11l1_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1l1ll1ll1l1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1l_opy_ (u"ࠤ࠳ࠦዠ"),
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1l_opy_ (u"ࠥࠦዡ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll1lll1l_opy_.AISelfHealStep(req)
            self.logger.info(bstack1l_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨዢ") + str(r) + bstack1l_opy_ (u"ࠧࠨዣ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦዤ") + str(e) + bstack1l_opy_ (u"ࠢࠣዥ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1l11ll_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1l1ll1l1111_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1l_opy_ (u"ࠣ࠲ࠥዦ")):
        self.bstack1lllll1l111_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll1lll1l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1l_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦዧ") + str(r) + bstack1l_opy_ (u"ࠥࠦየ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤዩ") + str(e) + bstack1l_opy_ (u"ࠧࠨዪ"))
            traceback.print_exc()
            raise e