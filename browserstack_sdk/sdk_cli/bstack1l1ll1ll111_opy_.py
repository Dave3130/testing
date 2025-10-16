# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
    bstack1llllll11ll_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack111111111l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1ll1ll_opy_ import bstack1llllllll11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1l1111_opy_(bstack1llllllll11_opy_):
    bstack1l1ll1l11ll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack111111111l_opy_.bstack1llllll1l1l_opy_((bstack11111111ll_opy_.bstack1llll1l1ll1_opy_, bstack1lllllll1ll_opy_.PRE), self.bstack1lllllllll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllllllll1_opy_(
        self,
        f: bstack111111111l_opy_,
        driver: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll111l11l_opy_(hub_url):
            if not bstack1l1ll1l1111_opy_.bstack1l1ll1l11ll_opy_:
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࠥࡹࡥ࡭ࡨ࠰࡬ࡪࡧ࡬ࠡࡨ࡯ࡳࡼࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡮ࡴࡦࡳࡣࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥ࡮ࡵࡣࡡࡸࡶࡱࡃࠢወ") + str(hub_url) + bstack1ll1ll1_opy_ (u"ࠢࠣዉ"))
                bstack1l1ll1l1111_opy_.bstack1l1ll1l11ll_opy_ = True
            return
        command_name = f.bstack1l1lll11lll_opy_(*args)
        bstack1l1lll111l1_opy_ = f.bstack1l1lll1l1ll_opy_(*args)
        if command_name and command_name.lower() == bstack1ll1ll1_opy_ (u"ࠣࡨ࡬ࡲࡩ࡫࡬ࡦ࡯ࡨࡲࡹࠨዊ") and bstack1l1lll111l1_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll111l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠤࡸࡷ࡮ࡴࡧࠣዋ"), None), bstack1l1lll111l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤዌ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠦࢀࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࢁ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡰࡴࠣࡥࡷ࡭ࡳ࠯ࡷࡶ࡭ࡳ࡭࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡࡱࡵࠤࡦࡸࡧࡴ࠰ࡹࡥࡱࡻࡥ࠾ࠤው") + str(locator_value) + bstack1ll1ll1_opy_ (u"ࠧࠨዎ"))
                return
            def bstack1l1ll1l1lll_opy_(driver, bstack1l1ll1l11l1_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll1l11l1_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll1ll11l_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1ll1ll1_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࠤዏ") + str(locator_value) + bstack1ll1ll1_opy_ (u"ࠢࠣዐ"))
                    else:
                        self.logger.warning(bstack1ll1ll1_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴ࠯ࡱࡳ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࡀࠦዑ") + str(response) + bstack1ll1ll1_opy_ (u"ࠤࠥዒ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1ll1l1_opy_(
                        driver, bstack1l1ll1l11l1_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1l1lll_opy_.__name__ = command_name
            return bstack1l1ll1l1lll_opy_
    def __1l1ll1ll1l1_opy_(
        self,
        driver,
        bstack1l1ll1l11l1_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll1ll11l_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1ll1ll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡺࡲࡪࡩࡪࡩࡷ࡫ࡤ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࠥዓ") + str(locator_value) + bstack1ll1ll1_opy_ (u"ࠦࠧዔ"))
                bstack1l1ll1l1ll1_opy_ = self.bstack1l1ll1l1l11_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1ll1ll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣ࡬ࡪࡧ࡬ࡪࡰࡪࡣࡷ࡫ࡳࡶ࡮ࡷࡁࠧዕ") + str(bstack1l1ll1l1ll1_opy_) + bstack1ll1ll1_opy_ (u"ࠨࠢዖ"))
                if bstack1l1ll1l1ll1_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1ll1ll1_opy_ (u"ࠢࡶࡵ࡬ࡲ࡬ࠨ዗"): bstack1l1ll1l1ll1_opy_.locator_type,
                            bstack1ll1ll1_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢዘ"): bstack1l1ll1l1ll1_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1l11l1_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1ll1ll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡌࡣࡉࡋࡂࡖࡉࠥዙ"), False):
                    self.logger.info(bstack1lll1ll111l_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠲ࡳࡩࡴࡵ࡬ࡲ࡬ࡀࠠࡴ࡮ࡨࡩࡵ࠮࠳࠱ࠫࠣࡰࡪࡺࡴࡪࡰࡪࠤࡾࡵࡵࠡ࡫ࡱࡷࡵ࡫ࡣࡵࠢࡷ࡬ࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡦࡺࡷࡩࡳࡹࡩࡰࡰࠣࡰࡴ࡭ࡳࠣዚ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1ll1ll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢዛ") + str(response) + bstack1ll1ll1_opy_ (u"ࠧࠨዜ"))
        except Exception as err:
            self.logger.warning(bstack1ll1ll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠻ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥዝ") + str(err) + bstack1ll1ll1_opy_ (u"ࠢࠣዞ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll1l1l1l_opy_, stage=STAGE.bstack111l1l111_opy_)
    def bstack1l1ll1ll11l_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1ll1ll1_opy_ (u"ࠣ࠲ࠥዟ"),
    ):
        self.bstack1llllll111l_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1ll1ll1_opy_ (u"ࠤࠥዠ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1lllll1lll1_opy_.AISelfHealStep(req)
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧዡ") + str(r) + bstack1ll1ll1_opy_ (u"ࠦࠧዢ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥዣ") + str(e) + bstack1ll1ll1_opy_ (u"ࠨࠢዤ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1l111l_opy_, stage=STAGE.bstack111l1l111_opy_)
    def bstack1l1ll1l1l11_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1ll1ll1_opy_ (u"ࠢ࠱ࠤዥ")):
        self.bstack1llllll111l_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1lllll1lll1_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1ll1ll1_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥዦ") + str(r) + bstack1ll1ll1_opy_ (u"ࠤࠥዧ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1ll1_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣየ") + str(e) + bstack1ll1ll1_opy_ (u"ࠦࠧዩ"))
            traceback.print_exc()
            raise e