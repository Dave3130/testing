# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
    bstack1llllllll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll11l11_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1l1l11_opy_(bstack1llll1lll1l_opy_):
    bstack1l1ll1l1l1l_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.PRE), self.bstack1llllll1ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllll1ll1_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll1111l11_opy_(hub_url):
            if not bstack1l1ll1l1l11_opy_.bstack1l1ll1l1l1l_opy_:
                self.logger.warning(bstack1ll1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࠥࡹࡥ࡭ࡨ࠰࡬ࡪࡧ࡬ࠡࡨ࡯ࡳࡼࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡮ࡴࡦࡳࡣࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥ࡮ࡵࡣࡡࡸࡶࡱࡃࠢ዁") + str(hub_url) + bstack1ll1l_opy_ (u"ࠢࠣዂ"))
                bstack1l1ll1l1l11_opy_.bstack1l1ll1l1l1l_opy_ = True
            return
        command_name = f.bstack1l1lll1l11l_opy_(*args)
        bstack1l1llll1111_opy_ = f.bstack1l1llll111l_opy_(*args)
        if command_name and command_name.lower() == bstack1ll1l_opy_ (u"ࠣࡨ࡬ࡲࡩ࡫࡬ࡦ࡯ࡨࡲࡹࠨዃ") and bstack1l1llll1111_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1llll1111_opy_.get(bstack1ll1l_opy_ (u"ࠤࡸࡷ࡮ࡴࡧࠣዄ"), None), bstack1l1llll1111_opy_.get(bstack1ll1l_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤዅ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1ll1l_opy_ (u"ࠦࢀࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࢁ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡰࡴࠣࡥࡷ࡭ࡳ࠯ࡷࡶ࡭ࡳ࡭࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡࡱࡵࠤࡦࡸࡧࡴ࠰ࡹࡥࡱࡻࡥ࠾ࠤ዆") + str(locator_value) + bstack1ll1l_opy_ (u"ࠧࠨ዇"))
                return
            def bstack1l1ll1ll11l_opy_(driver, bstack1l1ll1l11ll_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll1l11ll_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll1l111l_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1ll1l_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࠤወ") + str(locator_value) + bstack1ll1l_opy_ (u"ࠢࠣዉ"))
                    else:
                        self.logger.warning(bstack1ll1l_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴ࠯ࡱࡳ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࡀࠦዊ") + str(response) + bstack1ll1l_opy_ (u"ࠤࠥዋ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1ll111_opy_(
                        driver, bstack1l1ll1l11ll_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1ll11l_opy_.__name__ = command_name
            return bstack1l1ll1ll11l_opy_
    def __1l1ll1ll111_opy_(
        self,
        driver,
        bstack1l1ll1l11ll_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll1l111l_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1ll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡺࡲࡪࡩࡪࡩࡷ࡫ࡤ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࠥዌ") + str(locator_value) + bstack1ll1l_opy_ (u"ࠦࠧው"))
                bstack1l1ll1l11l1_opy_ = self.bstack1l1ll1l1ll1_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣ࡬ࡪࡧ࡬ࡪࡰࡪࡣࡷ࡫ࡳࡶ࡮ࡷࡁࠧዎ") + str(bstack1l1ll1l11l1_opy_) + bstack1ll1l_opy_ (u"ࠨࠢዏ"))
                if bstack1l1ll1l11l1_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1ll1l_opy_ (u"ࠢࡶࡵ࡬ࡲ࡬ࠨዐ"): bstack1l1ll1l11l1_opy_.locator_type,
                            bstack1ll1l_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢዑ"): bstack1l1ll1l11l1_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1l11ll_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1ll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡌࡣࡉࡋࡂࡖࡉࠥዒ"), False):
                    self.logger.info(bstack1lllll1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠲ࡳࡩࡴࡵ࡬ࡲ࡬ࡀࠠࡴ࡮ࡨࡩࡵ࠮࠳࠱ࠫࠣࡰࡪࡺࡴࡪࡰࡪࠤࡾࡵࡵࠡ࡫ࡱࡷࡵ࡫ࡣࡵࠢࡷ࡬ࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡦࡺࡷࡩࡳࡹࡩࡰࡰࠣࡰࡴ࡭ࡳࠣዓ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1ll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢዔ") + str(response) + bstack1ll1l_opy_ (u"ࠧࠨዕ"))
        except Exception as err:
            self.logger.warning(bstack1ll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠻ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥዖ") + str(err) + bstack1ll1l_opy_ (u"ࠢࠣ዗"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll11llll_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1l1ll1l111l_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1ll1l_opy_ (u"ࠣ࠲ࠥዘ"),
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1ll1l_opy_ (u"ࠤࠥዙ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll1l1ll1_opy_.AISelfHealStep(req)
            self.logger.info(bstack1ll1l_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧዚ") + str(r) + bstack1ll1l_opy_ (u"ࠦࠧዛ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥዜ") + str(e) + bstack1ll1l_opy_ (u"ࠨࠢዝ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1l1lll_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1l1ll1l1ll1_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1ll1l_opy_ (u"ࠢ࠱ࠤዞ")):
        self.bstack1lllll1l111_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll1l1ll1_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1ll1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥዟ") + str(r) + bstack1ll1l_opy_ (u"ࠤࠥዠ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣዡ") + str(e) + bstack1ll1l_opy_ (u"ࠦࠧዢ"))
            traceback.print_exc()
            raise e