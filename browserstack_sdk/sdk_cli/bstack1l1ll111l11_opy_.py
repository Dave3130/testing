# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lllll111ll_opy_,
    bstack1llllll1l11_opy_,
    bstack1llll11l11l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll1l11l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import bstack1llllll111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11l1l1_opy_(bstack1llllll111l_opy_):
    bstack1l1ll11l1ll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll1l11l_opy_.bstack1lllll1llll_opy_((bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_, bstack1llllll1l11_opy_.PRE), self.bstack1lllll11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll11ll1_opy_(
        self,
        f: bstack1lllll1l11l_opy_,
        driver: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1llll111_opy_(hub_url):
            if not bstack1l1ll11l1l1_opy_.bstack1l1ll11l1ll_opy_:
                self.logger.warning(bstack11lll1_opy_ (u"ࠧࡲ࡯ࡤࡣ࡯ࠤࡸ࡫࡬ࡧ࠯࡫ࡩࡦࡲࠠࡧ࡮ࡲࡻࠥࡪࡩࡴࡣࡥࡰࡪࡪࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣ࡭ࡳ࡬ࡲࡢࠢࡶࡩࡸࡹࡩࡰࡰࡶࠤ࡭ࡻࡢࡠࡷࡵࡰࡂࠨዣ") + str(hub_url) + bstack11lll1_opy_ (u"ࠨࠢዤ"))
                bstack1l1ll11l1l1_opy_.bstack1l1ll11l1ll_opy_ = True
            return
        command_name = f.bstack1l1lll1l11l_opy_(*args)
        bstack1l1ll1lll11_opy_ = f.bstack1l1ll1ll1l1_opy_(*args)
        if command_name and command_name.lower() == bstack11lll1_opy_ (u"ࠢࡧ࡫ࡱࡨࡪࡲࡥ࡮ࡧࡱࡸࠧዥ") and bstack1l1ll1lll11_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1ll1lll11_opy_.get(bstack11lll1_opy_ (u"ࠣࡷࡶ࡭ࡳ࡭ࠢዦ"), None), bstack1l1ll1lll11_opy_.get(bstack11lll1_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣዧ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11lll1_opy_ (u"ࠥࡿࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࢀ࠾ࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠦ࡯ࡳࠢࡤࡶ࡬ࡹ࠮ࡶࡵ࡬ࡲ࡬ࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠࡰࡴࠣࡥࡷ࡭ࡳ࠯ࡸࡤࡰࡺ࡫࠽ࠣየ") + str(locator_value) + bstack11lll1_opy_ (u"ࠦࠧዩ"))
                return
            def bstack1l1ll11l11l_opy_(driver, bstack1l1ll11lll1_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11lll1_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll111lll_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11lll1_opy_ (u"ࠧࡹࡵࡤࡥࡨࡷࡸ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࠣዪ") + str(locator_value) + bstack11lll1_opy_ (u"ࠨࠢያ"))
                    else:
                        self.logger.warning(bstack11lll1_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳ࠮ࡰࡲ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠿ࠥዬ") + str(response) + bstack11lll1_opy_ (u"ࠣࠤይ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll11ll1l_opy_(
                        driver, bstack1l1ll11lll1_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll11l11l_opy_.__name__ = command_name
            return bstack1l1ll11l11l_opy_
    def __1l1ll11ll1l_opy_(
        self,
        driver,
        bstack1l1ll11lll1_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll111lll_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡹࡸࡩࡨࡩࡨࡶࡪࡪ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࠤዮ") + str(locator_value) + bstack11lll1_opy_ (u"ࠥࠦዯ"))
                bstack1l1ll111l1l_opy_ = self.bstack1l1ll11ll11_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢ࡫ࡩࡦࡲࡩ࡯ࡩࡢࡶࡪࡹࡵ࡭ࡶࡀࠦደ") + str(bstack1l1ll111l1l_opy_) + bstack11lll1_opy_ (u"ࠧࠨዱ"))
                if bstack1l1ll111l1l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11lll1_opy_ (u"ࠨࡵࡴ࡫ࡱ࡫ࠧዲ"): bstack1l1ll111l1l_opy_.locator_type,
                            bstack11lll1_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨዳ"): bstack1l1ll111l1l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11lll1_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡋࡢࡈࡊࡈࡕࡈࠤዴ"), False):
                    self.logger.info(bstack1lll1ll1111_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠱ࡲ࡯ࡳࡴ࡫ࡱ࡫࠿ࠦࡳ࡭ࡧࡨࡴ࠭࠹࠰ࠪࠢ࡯ࡩࡹࡺࡩ࡯ࡩࠣࡽࡴࡻࠠࡪࡰࡶࡴࡪࡩࡴࠡࡶ࡫ࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࠢ࡯ࡳ࡬ࡹࠢድ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11lll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱ࡳࡵ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣࡶࡪࡹࡰࡰࡰࡶࡩࡂࠨዶ") + str(response) + bstack11lll1_opy_ (u"ࠦࠧዷ"))
        except Exception as err:
            self.logger.warning(bstack11lll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠺ࠡࡧࡵࡶࡴࡸ࠺ࠡࠤዸ") + str(err) + bstack11lll1_opy_ (u"ࠨࠢዹ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll11l111_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack1l1ll111lll_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11lll1_opy_ (u"ࠢ࠱ࠤዺ"),
    ):
        self.bstack1llll1ll1ll_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11lll1_opy_ (u"ࠣࠤዻ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll11lll1_opy_.AISelfHealStep(req)
            self.logger.info(bstack11lll1_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦዼ") + str(r) + bstack11lll1_opy_ (u"ࠥࠦዽ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤዾ") + str(e) + bstack11lll1_opy_ (u"ࠧࠨዿ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll111ll1_opy_, stage=STAGE.bstack11ll1ll11_opy_)
    def bstack1l1ll11ll11_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11lll1_opy_ (u"ࠨ࠰ࠣጀ")):
        self.bstack1llll1ll1ll_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll11lll1_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11lll1_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࠤጁ") + str(r) + bstack11lll1_opy_ (u"ࠣࠤጂ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11lll1_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢጃ") + str(e) + bstack11lll1_opy_ (u"ࠥࠦጄ"))
            traceback.print_exc()
            raise e