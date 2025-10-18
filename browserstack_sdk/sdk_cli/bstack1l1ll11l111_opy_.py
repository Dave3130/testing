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
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
    bstack1llll1l1111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import bstack1lllll11l1l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1ll11l_opy_ import bstack1llll1l1l11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11ll11_opy_(bstack1llll1l1l11_opy_):
    bstack1l1ll11l1ll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll11l1l_opy_.bstack1lllllll11l_opy_((bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_, bstack1llll1l1lll_opy_.PRE), self.bstack1llllll1111_opy_)
    def is_enabled(self) -> bool:
        return True
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
        hub_url = f.hub_url(driver)
        if f.bstack1ll1llll1l1_opy_(hub_url):
            if not bstack1l1ll11ll11_opy_.bstack1l1ll11l1ll_opy_:
                self.logger.warning(bstack11l111_opy_ (u"ࠦࡱࡵࡣࡢ࡮ࠣࡷࡪࡲࡦ࠮ࡪࡨࡥࡱࠦࡦ࡭ࡱࡺࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢ࡬ࡲ࡫ࡸࡡࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧዩ") + str(hub_url) + bstack11l111_opy_ (u"ࠧࠨዪ"))
                bstack1l1ll11ll11_opy_.bstack1l1ll11l1ll_opy_ = True
            return
        command_name = f.bstack1l1lll1111l_opy_(*args)
        bstack1l1ll1l1l11_opy_ = f.bstack1l1ll1ll1l1_opy_(*args)
        if command_name and command_name.lower() == bstack11l111_opy_ (u"ࠨࡦࡪࡰࡧࡩࡱ࡫࡭ࡦࡰࡷࠦያ") and bstack1l1ll1l1l11_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1ll1l1l11_opy_.get(bstack11l111_opy_ (u"ࠢࡶࡵ࡬ࡲ࡬ࠨዬ"), None), bstack1l1ll1l1l11_opy_.get(bstack11l111_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢይ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11l111_opy_ (u"ࠤࡾࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦࡿ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡵࡲࠡࡣࡵ࡫ࡸ࠴ࡵࡴ࡫ࡱ࡫ࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡯ࡳࠢࡤࡶ࡬ࡹ࠮ࡷࡣ࡯ࡹࡪࡃࠢዮ") + str(locator_value) + bstack11l111_opy_ (u"ࠥࠦዯ"))
                return
            def bstack1l1ll11l11l_opy_(driver, bstack1l1ll11llll_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11llll_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll11ll1l_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11l111_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࠢደ") + str(locator_value) + bstack11l111_opy_ (u"ࠧࠨዱ"))
                    else:
                        self.logger.warning(bstack11l111_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ࠭࡯ࡱ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠾ࠤዲ") + str(response) + bstack11l111_opy_ (u"ࠢࠣዳ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll111lll_opy_(
                        driver, bstack1l1ll11llll_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll11l11l_opy_.__name__ = command_name
            return bstack1l1ll11l11l_opy_
    def __1l1ll111lll_opy_(
        self,
        driver,
        bstack1l1ll11llll_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll11ll1l_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11l111_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡸࡷ࡯ࡧࡨࡧࡵࡩࡩࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࠣዴ") + str(locator_value) + bstack11l111_opy_ (u"ࠤࠥድ"))
                bstack1l1ll11l1l1_opy_ = self.bstack1l1ll111l1l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡪࡨࡥࡱ࡯࡮ࡨࡡࡵࡩࡸࡻ࡬ࡵ࠿ࠥዶ") + str(bstack1l1ll11l1l1_opy_) + bstack11l111_opy_ (u"ࠦࠧዷ"))
                if bstack1l1ll11l1l1_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11l111_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦዸ"): bstack1l1ll11l1l1_opy_.locator_type,
                            bstack11l111_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧዹ"): bstack1l1ll11l1l1_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11llll_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡊࡡࡇࡉࡇ࡛ࡇࠣዺ"), False):
                    self.logger.info(bstack11l1ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠰ࡱ࡮ࡹࡳࡪࡰࡪ࠾ࠥࡹ࡬ࡦࡧࡳࠬ࠸࠶ࠩࠡ࡮ࡨࡸࡹ࡯࡮ࡨࠢࡼࡳࡺࠦࡩ࡯ࡵࡳࡩࡨࡺࠠࡵࡪࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࠡ࡮ࡲ࡫ࡸࠨዻ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰ࡲࡴ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࡁࠧዼ") + str(response) + bstack11l111_opy_ (u"ࠥࠦዽ"))
        except Exception as err:
            self.logger.warning(bstack11l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹࡀࠠࡦࡴࡵࡳࡷࡀࠠࠣዾ") + str(err) + bstack11l111_opy_ (u"ࠧࠨዿ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll111ll1_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1l1ll11ll1l_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11l111_opy_ (u"ࠨ࠰ࠣጀ"),
    ):
        self.bstack1llll1lll11_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11l111_opy_ (u"ࠢࠣጁ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llllll1l11_opy_.AISelfHealStep(req)
            self.logger.info(bstack11l111_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥጂ") + str(r) + bstack11l111_opy_ (u"ࠤࠥጃ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣጄ") + str(e) + bstack11l111_opy_ (u"ࠦࠧጅ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11lll1_opy_, stage=STAGE.bstack1l11lll11_opy_)
    def bstack1l1ll111l1l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11l111_opy_ (u"ࠧ࠶ࠢጆ")):
        self.bstack1llll1lll11_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llllll1l11_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11l111_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣጇ") + str(r) + bstack11l111_opy_ (u"ࠢࠣገ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨጉ") + str(e) + bstack11l111_opy_ (u"ࠤࠥጊ"))
            traceback.print_exc()
            raise e