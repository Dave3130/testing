# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import (
    bstack1llll1lll11_opy_,
    bstack1llll1ll111_opy_,
    bstack1llllllll1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import bstack1lllll111l1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1111111ll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1l11l1_opy_(bstack1111111ll1_opy_):
    bstack1l1ll11llll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll111l1_opy_.bstack1llllll1111_opy_((bstack1llll1lll11_opy_.bstack1llllllllll_opy_, bstack1llll1ll111_opy_.PRE), self.bstack1111111111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1111111111_opy_(
        self,
        f: bstack1lllll111l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1lllll1llll_opy_: Tuple[bstack1llll1lll11_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll111l111_opy_(hub_url):
            if not bstack1l1ll1l11l1_opy_.bstack1l1ll11llll_opy_:
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠢ࡭ࡱࡦࡥࡱࠦࡳࡦ࡮ࡩ࠱࡭࡫ࡡ࡭ࠢࡩࡰࡴࡽࠠࡥ࡫ࡶࡥࡧࡲࡥࡥࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥ࡯࡮ࡧࡴࡤࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣዂ") + str(hub_url) + bstack1l1lll1_opy_ (u"ࠣࠤዃ"))
                bstack1l1ll1l11l1_opy_.bstack1l1ll11llll_opy_ = True
            return
        command_name = f.bstack1l1llll11l1_opy_(*args)
        bstack1l1lll11lll_opy_ = f.bstack1l1lll1l1ll_opy_(*args)
        if command_name and command_name.lower() == bstack1l1lll1_opy_ (u"ࠤࡩ࡭ࡳࡪࡥ࡭ࡧࡰࡩࡳࡺࠢዄ") and bstack1l1lll11lll_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll11lll_opy_.get(bstack1l1lll1_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤዅ"), None), bstack1l1lll11lll_opy_.get(bstack1l1lll1_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥ዆"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠧࢁࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࢂࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡱࡵࠤࡦࡸࡧࡴ࠰ࡸࡷ࡮ࡴࡧ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢࡲࡶࠥࡧࡲࡨࡵ࠱ࡺࡦࡲࡵࡦ࠿ࠥ዇") + str(locator_value) + bstack1l1lll1_opy_ (u"ࠨࠢወ"))
                return
            def bstack1l1ll1l1l1l_opy_(driver, bstack1l1ll11ll1l_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11ll1l_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll11lll1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1l1lll1_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳ࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࠥዉ") + str(locator_value) + bstack1l1lll1_opy_ (u"ࠣࠤዊ"))
                    else:
                        self.logger.warning(bstack1l1lll1_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡲࡴ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࡁࠧዋ") + str(response) + bstack1l1lll1_opy_ (u"ࠥࠦዌ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1l111l_opy_(
                        driver, bstack1l1ll11ll1l_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1l1l1l_opy_.__name__ = command_name
            return bstack1l1ll1l1l1l_opy_
    def __1l1ll1l111l_opy_(
        self,
        driver,
        bstack1l1ll11ll1l_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll11lll1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1l1lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡴࡳ࡫ࡪ࡫ࡪࡸࡥࡥ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࠦው") + str(locator_value) + bstack1l1lll1_opy_ (u"ࠧࠨዎ"))
                bstack1l1ll1l1l11_opy_ = self.bstack1l1ll1l1ll1_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤ࡭࡫ࡡ࡭࡫ࡱ࡫ࡤࡸࡥࡴࡷ࡯ࡸࡂࠨዏ") + str(bstack1l1ll1l1l11_opy_) + bstack1l1lll1_opy_ (u"ࠢࠣዐ"))
                if bstack1l1ll1l1l11_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1l1lll1_opy_ (u"ࠣࡷࡶ࡭ࡳ࡭ࠢዑ"): bstack1l1ll1l1l11_opy_.locator_type,
                            bstack1l1lll1_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣዒ"): bstack1l1ll1l1l11_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11ll1l_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1l1lll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡍࡤࡊࡅࡃࡗࡊࠦዓ"), False):
                    self.logger.info(bstack1lll1ll1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹ࠳࡭ࡪࡵࡶ࡭ࡳ࡭࠺ࠡࡵ࡯ࡩࡪࡶࠨ࠴࠲ࠬࠤࡱ࡫ࡴࡵ࡫ࡱ࡫ࠥࡿ࡯ࡶࠢ࡬ࡲࡸࡶࡥࡤࡶࠣࡸ࡭࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡧࡻࡸࡪࡴࡳࡪࡱࡱࠤࡱࡵࡧࡴࠤዔ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1l1lll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳࡮ࡰ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠽ࠣዕ") + str(response) + bstack1l1lll1_opy_ (u"ࠨࠢዖ"))
        except Exception as err:
            self.logger.warning(bstack1l1lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠼ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠦ዗") + str(err) + bstack1l1lll1_opy_ (u"ࠣࠤዘ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll1l11ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l1ll11lll1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1l1lll1_opy_ (u"ࠤ࠳ࠦዙ"),
    ):
        self.bstack1llll1llll1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1l1lll1_opy_ (u"ࠥࠦዚ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1lllll1ll11_opy_.AISelfHealStep(req)
            self.logger.info(bstack1l1lll1_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨዛ") + str(r) + bstack1l1lll1_opy_ (u"ࠧࠨዜ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦዝ") + str(e) + bstack1l1lll1_opy_ (u"ࠢࠣዞ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1l1111_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l1ll1l1ll1_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1l1lll1_opy_ (u"ࠣ࠲ࠥዟ")):
        self.bstack1llll1llll1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1lllll1ll11_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1l1lll1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦዠ") + str(r) + bstack1l1lll1_opy_ (u"ࠥࠦዡ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤዢ") + str(e) + bstack1l1lll1_opy_ (u"ࠧࠨዣ"))
            traceback.print_exc()
            raise e