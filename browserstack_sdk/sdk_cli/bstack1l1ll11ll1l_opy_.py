# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllllll11l_opy_ import bstack1lllllllll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11lll1_opy_(bstack1lllllllll1_opy_):
    bstack1l1ll11ll11_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll1l1l1_opy_.bstack1lllll1l1ll_opy_((bstack1llll1ll1l1_opy_.bstack1llll1lllll_opy_, bstack1lllll1ll1l_opy_.PRE), self.bstack1llll1lll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llll1lll1l_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1llll11l_opy_(hub_url):
            if not bstack1l1ll11lll1_opy_.bstack1l1ll11ll11_opy_:
                self.logger.warning(bstack11ll_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࠥࡹࡥ࡭ࡨ࠰࡬ࡪࡧ࡬ࠡࡨ࡯ࡳࡼࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡮ࡴࡦࡳࡣࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥ࡮ࡵࡣࡡࡸࡶࡱࡃࠢያ") + str(hub_url) + bstack11ll_opy_ (u"ࠢࠣዬ"))
                bstack1l1ll11lll1_opy_.bstack1l1ll11ll11_opy_ = True
            return
        command_name = f.bstack1l1lll11l11_opy_(*args)
        bstack1l1ll1llll1_opy_ = f.bstack1l1lll11lll_opy_(*args)
        if command_name and command_name.lower() == bstack11ll_opy_ (u"ࠣࡨ࡬ࡲࡩ࡫࡬ࡦ࡯ࡨࡲࡹࠨይ") and bstack1l1ll1llll1_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1ll1llll1_opy_.get(bstack11ll_opy_ (u"ࠤࡸࡷ࡮ࡴࡧࠣዮ"), None), bstack1l1ll1llll1_opy_.get(bstack11ll_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤዯ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11ll_opy_ (u"ࠦࢀࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࢁ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡰࡴࠣࡥࡷ࡭ࡳ࠯ࡷࡶ࡭ࡳ࡭࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡࡱࡵࠤࡦࡸࡧࡴ࠰ࡹࡥࡱࡻࡥ࠾ࠤደ") + str(locator_value) + bstack11ll_opy_ (u"ࠧࠨዱ"))
                return
            def bstack1l1ll11l1l1_opy_(driver, bstack1l1ll11l111_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11l111_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll11l11l_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11ll_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࠤዲ") + str(locator_value) + bstack11ll_opy_ (u"ࠢࠣዳ"))
                    else:
                        self.logger.warning(bstack11ll_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴ࠯ࡱࡳ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࡀࠦዴ") + str(response) + bstack11ll_opy_ (u"ࠤࠥድ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll111l1l_opy_(
                        driver, bstack1l1ll11l111_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll11l1l1_opy_.__name__ = command_name
            return bstack1l1ll11l1l1_opy_
    def __1l1ll111l1l_opy_(
        self,
        driver,
        bstack1l1ll11l111_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll11l11l_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡺࡲࡪࡩࡪࡩࡷ࡫ࡤ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࠥዶ") + str(locator_value) + bstack11ll_opy_ (u"ࠦࠧዷ"))
                bstack1l1ll11l1ll_opy_ = self.bstack1l1ll111lll_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣ࡬ࡪࡧ࡬ࡪࡰࡪࡣࡷ࡫ࡳࡶ࡮ࡷࡁࠧዸ") + str(bstack1l1ll11l1ll_opy_) + bstack11ll_opy_ (u"ࠨࠢዹ"))
                if bstack1l1ll11l1ll_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11ll_opy_ (u"ࠢࡶࡵ࡬ࡲ࡬ࠨዺ"): bstack1l1ll11l1ll_opy_.locator_type,
                            bstack11ll_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢዻ"): bstack1l1ll11l1ll_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11l111_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡌࡣࡉࡋࡂࡖࡉࠥዼ"), False):
                    self.logger.info(bstack11l1llll_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠲ࡳࡩࡴࡵ࡬ࡲ࡬ࡀࠠࡴ࡮ࡨࡩࡵ࠮࠳࠱ࠫࠣࡰࡪࡺࡴࡪࡰࡪࠤࡾࡵࡵࠡ࡫ࡱࡷࡵ࡫ࡣࡵࠢࡷ࡬ࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡦࡺࡷࡩࡳࡹࡩࡰࡰࠣࡰࡴ࡭ࡳࠣዽ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢዾ") + str(response) + bstack11ll_opy_ (u"ࠧࠨዿ"))
        except Exception as err:
            self.logger.warning(bstack11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠻ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥጀ") + str(err) + bstack11ll_opy_ (u"ࠢࠣጁ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll111ll1_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1l1ll11l11l_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11ll_opy_ (u"ࠣ࠲ࠥጂ"),
    ):
        self.bstack1lllll111ll_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11ll_opy_ (u"ࠤࠥጃ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1lllll11111_opy_.AISelfHealStep(req)
            self.logger.info(bstack11ll_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧጄ") + str(r) + bstack11ll_opy_ (u"ࠦࠧጅ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥጆ") + str(e) + bstack11ll_opy_ (u"ࠨࠢጇ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll111l11_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def bstack1l1ll111lll_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11ll_opy_ (u"ࠢ࠱ࠤገ")):
        self.bstack1lllll111ll_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1lllll11111_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11ll_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥጉ") + str(r) + bstack11ll_opy_ (u"ࠤࠥጊ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11ll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣጋ") + str(e) + bstack11ll_opy_ (u"ࠦࠧጌ"))
            traceback.print_exc()
            raise e