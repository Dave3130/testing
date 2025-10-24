# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1llll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11ll1l_opy_ import (
    bstack1llllll111l_opy_,
    bstack1llll1l111l_opy_,
    bstack1llllll1l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1111111l11_opy_ import bstack1llll1l11l1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll1lll_opy_ import bstack1llll1llll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1l111l_opy_(bstack1llll1llll1_opy_):
    bstack1l1ll11llll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llll1l11l1_opy_.bstack1llll1ll1l1_opy_((bstack1llllll111l_opy_.bstack1lllllll111_opy_, bstack1llll1l111l_opy_.PRE), self.bstack1lllll11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll11ll1_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llllll1l1l_opy_, str],
        bstack1lllll1l1l1_opy_: Tuple[bstack1llllll111l_opy_, bstack1llll1l111l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll1111111_opy_(hub_url):
            if not bstack1l1ll1l111l_opy_.bstack1l1ll11llll_opy_:
                self.logger.warning(bstack1l1_opy_ (u"ࠧࡲ࡯ࡤࡣ࡯ࠤࡸ࡫࡬ࡧ࠯࡫ࡩࡦࡲࠠࡧ࡮ࡲࡻࠥࡪࡩࡴࡣࡥࡰࡪࡪࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣ࡭ࡳ࡬ࡲࡢࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤ࡭ࡻࡢࡠࡷࡵࡰࡂࠨዜ") + str(hub_url) + bstack1l1_opy_ (u"ࠨࠢዝ"))
                bstack1l1ll1l111l_opy_.bstack1l1ll11llll_opy_ = True
            return
        command_name = f.bstack1l1lll11ll1_opy_(*args)
        bstack1l1ll1lll1l_opy_ = f.bstack1l1ll1llll1_opy_(*args)
        if command_name and command_name.lower() == bstack1l1_opy_ (u"ࠢࡧ࡫ࡱࡨࡪࡲࡥ࡮ࡧࡱࡸࠧዞ") and bstack1l1ll1lll1l_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1ll1lll1l_opy_.get(bstack1l1_opy_ (u"ࠣࡷࡶ࡭ࡳ࡭ࠢዟ"), None), bstack1l1ll1lll1l_opy_.get(bstack1l1_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣዠ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1l1_opy_ (u"ࠥࡿࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࢀ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠦ࡯ࡳࠢࡤࡶ࡬ࡹ࠮ࡶࡵ࡬ࡲ࡬ࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠࡰࡴࠣࡥࡷ࡭ࡳ࠯ࡸࡤࡰࡺ࡫࠽ࠣዡ") + str(locator_value) + bstack1l1_opy_ (u"ࠦࠧዢ"))
                return
            def bstack1l1ll11lll1_opy_(driver, bstack1l1ll11l1ll_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11l1ll_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll11l1l1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1l1_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࠣዣ") + str(locator_value) + bstack1l1_opy_ (u"ࠨࠢዤ"))
                    else:
                        self.logger.warning(bstack1l1_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳ࠮ࡰࡲ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠿ࠥዥ") + str(response) + bstack1l1_opy_ (u"ࠣࠤዦ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1l1111_opy_(
                        driver, bstack1l1ll11l1ll_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll11lll1_opy_.__name__ = command_name
            return bstack1l1ll11lll1_opy_
    def __1l1ll1l1111_opy_(
        self,
        driver,
        bstack1l1ll11l1ll_opy_: Callable,
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
                self.logger.info(bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡹࡸࡩࡨࡩࡨࡶࡪࡪ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࠤዧ") + str(locator_value) + bstack1l1_opy_ (u"ࠥࠦየ"))
                bstack1l1ll111lll_opy_ = self.bstack1l1ll11ll11_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢ࡫ࡩࡦࡲࡩ࡯ࡩࡢࡶࡪࡹࡵ࡭ࡶࡀࠦዩ") + str(bstack1l1ll111lll_opy_) + bstack1l1_opy_ (u"ࠧࠨዪ"))
                if bstack1l1ll111lll_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1l1_opy_ (u"ࠨࡵࡴ࡫ࡱ࡫ࠧያ"): bstack1l1ll111lll_opy_.locator_type,
                            bstack1l1_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨዬ"): bstack1l1ll111lll_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11l1ll_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡋࡢࡈࡊࡈࡕࡈࠤይ"), False):
                    self.logger.info(bstack1lll1llll11_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠱ࡲ࡯ࡳࡴ࡫ࡱ࡫࠿ࠦࡳ࡭ࡧࡨࡴ࠭࠹࠰ࠪࠢ࡯ࡩࡹࡺࡩ࡯ࡩࠣࡽࡴࡻࠠࡪࡰࡶࡴࡪࡩࡴࠡࡶ࡫ࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࠢ࡯ࡳ࡬ࡹࠢዮ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1l1_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱ࡳࡵ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣࡶࡪࡹࡰࡰࡰࡶࡩࡂࠨዯ") + str(response) + bstack1l1_opy_ (u"ࠦࠧደ"))
        except Exception as err:
            self.logger.warning(bstack1l1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠺ࠡࡧࡵࡶࡴࡸ࠺ࠡࠤዱ") + str(err) + bstack1l1_opy_ (u"ࠨࠢዲ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll11ll1l_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1l1ll11l1l1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1l1_opy_ (u"ࠢ࠱ࠤዳ"),
    ):
        self.bstack1llll1l1l1l_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1l1_opy_ (u"ࠣࠤዴ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll1l11ll_opy_.AISelfHealStep(req)
            self.logger.info(bstack1l1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦድ") + str(r) + bstack1l1_opy_ (u"ࠥࠦዶ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤዷ") + str(e) + bstack1l1_opy_ (u"ࠧࠨዸ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11l11l_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
    def bstack1l1ll11ll11_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1l1_opy_ (u"ࠨ࠰ࠣዹ")):
        self.bstack1llll1l1l1l_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll1l11ll_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1l1_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤዺ") + str(r) + bstack1l1_opy_ (u"ࠣࠤዻ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢዼ") + str(e) + bstack1l1_opy_ (u"ࠥࠦዽ"))
            traceback.print_exc()
            raise e